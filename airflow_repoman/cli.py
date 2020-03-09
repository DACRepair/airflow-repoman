import click
from airflow.logging_config import log


@click.group()
def main():
    pass


@main.command(help="Initializes the plugin db tables")
def init():
    import os
    from airflow import settings
    from airflow_repoman.Common.models import Base
    try:
        Base.metadata.create_all(settings.engine)
        log.info("Initialized database.")

        dag_path = os.path.normpath(settings.conf.get('core', 'dags_folder'))
        os.mkdir(dag_path) if not os.path.isdir(dag_path) else None

    except Exception as E:
        log.error("Unable to initialize database: {}", format(str(E)))


@main.command(help="Sync Repos")
@click.option('--continuous', is_flag=True, help="Runs continuously")
def reposync(continuous):
    from airflow_repoman.CLI.reposync import click_callable

    click_callable(continuous)


print(__name__)

if __name__ == "__main__":
    main()
