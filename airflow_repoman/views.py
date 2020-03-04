from flask import Blueprint
from flask_appbuilder import ModelView
from flask_appbuilder.forms import DynamicForm, StringField, BooleanField, IntegerField
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, BS3PasswordFieldWidget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_babel import lazy_gettext
from wtforms import PasswordField
from wtforms.validators import DataRequired, Optional, NumberRange

from airflow_repoman.models import Repos

RepomanBlueprint = Blueprint("airflow_repoman",
                             __name__,
                             template_folder="templates",
                             static_folder="static",
                             static_url_path="/static/airflow_repoman")


class RepomanForm(DynamicForm):
    name = StringField(lazy_gettext('Repo Name'), widget=BS3TextFieldWidget(), validators=[DataRequired()])
    enabled = BooleanField(lazy_gettext('Repo Enabled'))
    remote_url = StringField(lazy_gettext('Repo URL'), widget=BS3TextFieldWidget(), validators=[DataRequired()])
    remote_branch = StringField(lazy_gettext('Repo Branch'), widget=BS3TextFieldWidget(), validators=[DataRequired()])
    remote_user = StringField(lazy_gettext('Repo Username'), widget=BS3TextFieldWidget(), validators=[Optional()])
    remote_pass = PasswordField(lazy_gettext('Repo Password'), widget=BS3PasswordFieldWidget(), validators=[Optional()])
    refresh = IntegerField(lazy_gettext('Refresh Interval'), widget=BS3TextFieldWidget(),
                           validators=[NumberRange(min=0)])


class RepomanView(ModelView):
    route_base = "/repo"
    datamodel = SQLAInterface(Repos)

    base_permissions = ['can_add', 'can_list', 'can_edit', 'can_delete']
    base_order = ('name', 'asc')

    label_columns = {'name': 'Repo Name', 'enabled': 'Repo Enabled', 'remote_url': 'Remote URL',
                     'remote_branch': 'Remote Branch', 'refresh': 'Refresh (Seconds)', 'last_updated': 'Last Updated'}

    search_columns = ['name', 'enabled', 'remote_url', 'remote_branch', 'last_updated']

    list_columns = ['name', 'enabled', 'remote_url', 'remote_branch', 'refresh', 'last_updated']

    add_columns = edit_columns = show_columns = ['name', 'enabled', 'remote_url', 'remote_branch', 'remote_user',
                                                 'remote_pass']
    show_columns.append('last_updated')
    # add_form = edit_form = RepomanForm
