from flask import Blueprint
from flask_appbuilder import ModelView
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, BS3PasswordFieldWidget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms import StringField, BooleanField, IntegerField, PasswordField
from wtforms.validators import DataRequired

from airflow_repoman.models import Repos

RepomanBlueprint = Blueprint("airflow_repoman",
                             __name__,
                             template_folder="templates",
                             static_folder="static",
                             static_url_path="/static/airflow_repoman")


class RepomanForm(DynamicForm):
    name = StringField('Repo Name', widget=BS3TextFieldWidget(), validators=[DataRequired()])
    enabled = BooleanField('Repo Enabled')

    remote_url = StringField('Repo URL', widget=BS3TextFieldWidget())
    remote_branch = StringField('Repo Branch', widget=BS3TextFieldWidget())
    remote_user = StringField('Repo Username', widget=BS3TextFieldWidget())
    remote_pass = PasswordField('Repo Password', widget=BS3PasswordFieldWidget())

    refresh = StringField('Refresh Interval', widget=BS3TextFieldWidget())


class RepomanView(ModelView):
    route_base = "/repos"
    datamodel = SQLAInterface(Repos)

    search_columns = ['name', 'enabled', 'remote_url', 'remote_branch', 'last_updated']

    label_columns = {'name': 'Repo Name', 'enabled': 'Repo Enabled', 'remote_url': 'Remote URL',
                     'remote_branch': 'Remote Branch', 'refresh': 'Refresh (Seconds)', 'last_updated': 'Last Updated'}
    list_columns = ['name', 'enabled', 'remote_url', 'remote_branch', 'refresh', 'last_updated']

    show_columns = ['name', 'enabled', 'remote_url', 'remote_branch', 'remote_user', 'remote_pass', 'refresh']
    add_columns = show_columns
    edit_columns = add_columns
    add_form = RepomanForm
    edit_form = RepomanForm
