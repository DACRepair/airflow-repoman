from airflow.www.forms import FlaskForm
from flask import Blueprint
from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, BS3PasswordFieldWidget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_babel import lazy_gettext
from wtforms import StringField, BooleanField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Optional, NumberRange

from airflow_repoman.models import Repos

RepomanBlueprint = Blueprint("airflow_repoman",
                             __name__,
                             template_folder="templates",
                             static_folder="static",
                             static_url_path="/static/airflow_repoman")


class RepomanForm(FlaskForm):
    name = StringField(lazy_gettext('Repo Name'), widget=BS3TextFieldWidget(), validators=[DataRequired()])
    enabled = BooleanField(lazy_gettext('Repo Enabled'))

    remote_url = StringField(lazy_gettext('Repo URL'), widget=BS3TextFieldWidget(), validators=[DataRequired()])
    remote_branch = StringField(lazy_gettext('Repo Branch'), widget=BS3TextFieldWidget(), validators=[DataRequired()])
    remote_user = StringField(lazy_gettext('Repo Username'), widget=BS3TextFieldWidget(), validators=[Optional()])
    remote_pass = PasswordField(lazy_gettext('Repo Password'), widget=BS3PasswordFieldWidget(), validators=[Optional()])

    refresh = IntegerField(lazy_gettext('Refresh Interval'), widget=BS3TextFieldWidget(),
                           validators=[NumberRange(min=0)])


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
