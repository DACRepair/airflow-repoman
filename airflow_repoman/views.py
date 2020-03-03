from flask import Blueprint
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from airflow_repoman.models import Repos

RepomanBlueprint = Blueprint(
    "airflow_repoman",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/airflow_repoman"
)


class RepomanView(ModelView):
    datamodel = SQLAInterface(Repos)
