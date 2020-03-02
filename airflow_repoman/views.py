from flask import Blueprint
from flask_appbuilder import BaseView, expose

RepomanBlueprint = Blueprint(
    "airflow_repoman",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/airflow_repoman"
)


class RepomanView(BaseView):
    default_view = "index"

    @expose('/')
    def index(self):
        return self.render_template('test.html')
