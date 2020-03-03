from airflow import settings
from airflow.plugins_manager import AirflowPlugin
from .views import RepomanView, RepomanBlueprint
from .models import Repos


class RepomanAirflowPlugin(AirflowPlugin):
    def __init__(self):
        super(RepomanAirflowPlugin, self).__init__()
        Repos.__table__.create(settings.engine, checkfirst=True)

    name = "airflow_repoman"
    flask_blueprints = [RepomanBlueprint]
    appbuilder_views = [{"name": "DAG Repos",
                         "category": "Admin",
                         "view": RepomanView()}]
