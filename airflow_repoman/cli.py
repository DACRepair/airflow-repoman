import click


@click.group()
def main():
    pass


@main.command()
def init():
    from airflow import settings
    from airflow_repoman.models import Base

    Base.metadata.create_all(settings.engine)
