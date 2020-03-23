"""
Logic used for the "reposync" subcommand
"""
import datetime
import glob
import os
import time

from airflow import settings
from airflow.logging_config import log
from sqlalchemy import func

from airflow_repoman.common.git import GitRepo, GitURL
from airflow_repoman.common.models import DAGRepo


def clean_path(path: str):
    """
    Recursively deletes a path
    :param path:
    :return:
    """
    path = os.path.normpath(path)
    for item in glob.glob(os.path.normpath(path + "/*")):
        if os.path.isfile(item):
            os.remove(item)
        if os.path.isdir(item):
            sub = glob.glob(os.path.normpath(item + "/*/"))
            sub.append(glob.glob(os.path.normpath(item + "/*")))
            if len(sub) > 0:
                clean_path(item)
                os.rmdir(item)
    os.rmdir(path)


def dagsync(no_delete: bool = False):
    """
    Syncs the DAGRepo model with the filesystem
    :param no_delete:
    :return:
    """
    dag_path = os.path.normpath(settings.conf.get('core', 'dags_folder'))

    session = settings.Session()
    repos = session.query(DAGRepo)
    for repo in repos.all():
        repo: DAGRepo

        repo_name = "repoman_{}_{}_{}".format(repo.name.replace(" ", "_"),
                                              repo.remote_branch.replace(" ", "_"),
                                              repo.id)
        repo_path = os.path.normpath("{}/{}".format(dag_path, repo_name))

        remote_url = str(GitURL(
            repo.remote_url,
            username=repo.remote_user,
            password=repo.remote_pass))

        git_repo = GitRepo(repo_path, remote_url, repo.remote_branch)

        now = datetime.datetime.utcnow()
        if repo.enabled:
            if git_repo.check_repo() and int((repo.last_checked - now).seconds) > repo.interval:
                log.info("Repo has updates: %s", repo.name)
                git_repo.update_repo()
                repo.last_checked = now
                repo.last_updated = now
            else:
                repo.last_checked = now
            session.commit()

    for folder in [x for x in glob.glob(os.path.normpath(dag_path + "/*/")) if
                   os.path.basename(x).startswith('repoman_')]:
        repo_id = folder.split("_")[-1]
        repo = session.query(DAGRepo).filter(DAGRepo.id == int(repo_id))
        if repo.count() < 1:
            if no_delete:
                clean_path(folder)

    interval = session.query(func.min(DAGRepo.interval))
    if interval.count() > 0:
        return int(interval.one()[0])
    else:
        return 60


def click_callable(continuous: bool = False, no_delete: bool = False):
    """
    The callable used to run the dag sync (what is actually run by click)
    :param continuous:
    :param no_delete:
    :return:
    """
    while True:
        interval = dagsync(no_delete)
        if continuous:
            log.debug("Sync complete. Sleeping %i seconds", interval)
            time.sleep(interval)
        else:
            break
