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
@click.option("")
def reposync():
    import os
    from airflow import settings
    from glob import glob

    dag_path = settings.conf.get('core', 'dags_folder')


if __name__ == "__main__":
    main()
