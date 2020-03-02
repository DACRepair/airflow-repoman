from airflow.plugins_manager import AirflowPlugin
from .views import TestView


class RepomanAirflowPlugin(AirflowPlugin):
    name = "airflow_repoman"
    admin_views = [{"name": "Repos",
                    "category": "Admin",
                    "view": TestView()}]
