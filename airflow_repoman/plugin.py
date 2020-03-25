"""
Airflow Web UI Plugin
"""

from airflow.plugins_manager import AirflowPlugin
from airflow.settings import engine, Session

from airflow_repoman.airflow.admin import DAGRepoAdminView
from airflow_repoman.airflow.appbuilder import DAGRepoView
from airflow_repoman.airflow.blueprint import repoman_blueprint
from airflow_repoman.common.models import DAGRepo


class RepomanAirflowPlugin(AirflowPlugin):
    """
    Airflow Plugin
    """

    def __init__(self):
        DAGRepo.__table__.create(engine, checkfirst=True)

        super(RepomanAirflowPlugin, self).__init__()

    name = "airflow_repoman"

    appbuilder_views = [{"name": "DAG Repos",
                         "category": "Admin",
                         "view": DAGRepoView()}]

    admin_views = [DAGRepoAdminView(DAGRepo, Session(), category="Admin", name="DAG Repos")]

    flask_blueprints = [repoman_blueprint]
