import click


@click.group()
def main():
    pass


@main.command()
def init():
    from .models import Base
    from airflow import settings
    Base.metadata.create_all(settings.engine)
