from airflow.plugins_manager import AirflowPlugin
from .views import RepomanView, RepomanBlueprint


class RepomanAirflowPlugin(AirflowPlugin):
    name = "airflow_repoman"
    flask_blueprints = [RepomanBlueprint]
    appbuilder_views = [{"name": "Repos",
                         "category": "Admin",
                         "view": RepomanView()}]
