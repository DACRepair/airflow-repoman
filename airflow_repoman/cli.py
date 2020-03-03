import click
from airflow.logging_config import log


@click.group()
def main():
    pass


@main.command(help="Initializes the plugin db tables")
def initdb():
    from airflow import settings
    from airflow_repoman.models import Base

    log.info(Base.metadata.create_all(settings.engine))


@main.command(help="")
def reposync():
    import os
    from glob import glob
    from airflow import settings
    from airflow_repoman.models import Repos

    dag_path = os.path.normpath(settings.conf.get('core', 'dags_folder'))
    os.mkdir(dag_path) if not os.path.isdir(dag_path) else None

    session = settings.Session()
    repos = session.query(Repos).filter(Repos.enabled)

    for path in glob(os.path.normpath(dag_path + "/*")):
        path = os.path.basename(path)
        print(path)



if __name__ == "__main__":
    main()
