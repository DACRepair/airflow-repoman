from airflow.plugins_manager import AirflowPlugin
from .views import TestView


class RepomanAirflowPlugin(AirflowPlugin):
    appbuilder_views = [{"name": "Repos",
                         "category": "Admin",
                         "view": TestView()}]
