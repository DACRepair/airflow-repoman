from flask import Blueprint
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from airflow_repoman.models import Repos

RepomanBlueprint = Blueprint("airflow_repoman",
                             __name__,
                             template_folder="templates",
                             static_folder="static",
                             static_url_path="/static/airflow_repoman")


class RepomanView(ModelView):
    route_base = "/repos"
    datamodel = SQLAInterface(Repos)

    search_columns = ['name', 'enabled', 'remote_url', 'remote_branch', 'last_updated']

    label_columns = {'name': 'Repo Name', 'enabled': 'Repo Enabled', 'remote_url': 'Remote URL',
                     'remote_branch': 'Remote Branch', 'refresh': 'Refresh (Seconds)', 'last_updated': 'Last Updated'}
    list_columns = ['name', 'enabled', 'remote_url', 'remote_branch', 'refresh', 'last_updated']
