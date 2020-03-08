import datetime
import os
from airflow import settings
from airflow_repoman.Common.models import DAGRepo
from airflow_repoman.Common.git import GitRepo, GitURL

dag_path = os.path.normpath(settings.conf.get('core', 'dags_folder'))
os.mkdir(dag_path) if not os.path.isdir(dag_path) else None

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
            git_repo.update_repo()
            repo.last_checked = now
            repo.last_updated = now
        else:
            repo.last_checked = now
        session.commit()
