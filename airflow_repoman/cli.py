import click
from airflow.logging_config import log


@click.group()
def main():
    pass


@main.command(help="Initializes the plugin db tables")
def initdb():
    from airflow import settings
    from airflow_repoman.models import Base
    try:
        Base.metadata.create_all(settings.engine)
        log.info("Initialized database.")
    except Exception as E:
        log.error("Unable to initialize database: {}", format(str(E)))


@main.command(help="")
def reposync():
    pass


if __name__ == "__main__":
    main()
