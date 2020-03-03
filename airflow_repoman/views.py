from flask import Blueprint
from airflow.www.views import AirflowModelView
from airflow_repoman.models import Repos

RepomanBlueprint = Blueprint(
    "airflow_repoman",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/airflow_repoman"
)


class RepomanView(AirflowModelView):
    route_base = "/repos"

    datamodel = AirflowModelView.CustomSQLAInterface(Repos)

    base_permissions = ['can_list']

    label_columns = {'name': 'Repo Name', 'enabled': 'Repo Enabled', 'remote_url': 'Remote URL',
                     'remote_branch': 'Remote Branch', 'refresh': 'Refresh (Seconds)', 'last_updated': 'Last Updated'}

    list_columns = ['name', 'enabled', 'remote_url', 'remote_branch', 'refresh', 'last_updated']
