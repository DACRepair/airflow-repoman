"""
Airflow Repoman CLI tool.
"""

import os

import click
from airflow import settings
from airflow.logging_config import log
from sqlalchemy.exc import SQLAlchemyError

from airflow_repoman.cli.reposync import click_callable
from airflow_repoman.common.models import Base


@click.group()
def main():
    """
    Main group for CLI tool.
    :return:
    """


@main.command(help="Initializes the plugin db tables")
def init():
    """
    init sub command
    :return:
    """
    try:
        Base.metadata.create_all(settings.engine)
        log.info("Initialized database.")

        dag_path = os.path.normpath(settings.conf.get('core', 'dags_folder'))
        if not os.path.isdir(dag_path):
            os.mkdir(dag_path)

    except SQLAlchemyError as error:
        log.error("Unable to initialize database: %s", str(error))


@main.command(help="Sync Repos")
@click.option('--continuous', is_flag=True, help="Runs continuously")
@click.option('--no-delete', is_flag=True, help="Don't delete DAG folders when removed")
def reposync(continuous, no_delete):
    """
    reposync subcommand
    :param continuous:
    :param no_delete:
    :return:
    """
    log.info("Initializing RepoSync...")
    click_callable(continuous, no_delete)


if __name__ == "__main__":
    main()
