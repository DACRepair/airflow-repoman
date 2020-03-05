from airflow import settings
from airflow.plugins_manager import AirflowPlugin
from .views import DAGRepoView
from .models import DAGRepo


class RepomanAirflowPlugin(AirflowPlugin):
    def __init__(self):
        super(RepomanAirflowPlugin, self).__init__()
        DAGRepo.__table__.create(settings.engine, checkfirst=True)

    name = "airflow_repoman"
    appbuilder_views = [{"name": "DAG Repos",
                         "category": "Admin",
                         "view": DAGRepoView()}]
