import datetime
import glob
import os
import time

from airflow import settings
from airflow.logging_config import log
from sqlalchemy import func

from airflow_repoman.Common.git import GitRepo, GitURL
from airflow_repoman.Common.models import DAGRepo


def dagsync():
    dag_path = os.path.normpath(settings.conf.get('core', 'dags_folder'))

    session = settings.Session()
    repos = session.query(DAGRepo)
    for repo in repos.all():
        repo: DAGRepo

        repo_name = "repoman_{}_{}".format(repo.name.replace(" ", "_"), repo.id)
        repo_path = os.path.normpath("{}/{}".format(dag_path, repo_name))

        remote_url = str(GitURL(repo.remote_url, username=repo.remote_user, password=repo.remote_pass))
        git_repo = GitRepo(repo_path, remote_url, repo.remote_branch)

        now = datetime.datetime.utcnow()
        if repo.enabled:
            if git_repo.check_repo() and int((repo.last_checked - now).seconds) > repo.interval:
                log.info("Repo has updates: {}".format(repo.name))
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
            os.rmdir(folder)

    interval = session.query(func.min(DAGRepo.interval))
    if interval.count() > 0:
        return int(interval.one()[0])
    else:
        return 69


def click_callable(loop: bool = False):
    while True:
        interval = dagsync()
        if loop:
            log.debug("Sync complete. Sleeping {} seconds".format(interval))
            time.sleep(interval)
        else:
            break
