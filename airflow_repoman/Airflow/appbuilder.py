from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, BS3PasswordFieldWidget
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_babel import lazy_gettext
from wtforms.fields import BooleanField, IntegerField, PasswordField, StringField
from wtforms.validators import DataRequired, Optional, NumberRange

from airflow_repoman.Common.models import DAGRepo


class DAGRepoForm(DynamicForm):
    name = StringField(lazy_gettext('Repo Name'), widget=BS3TextFieldWidget(), validators=[DataRequired()])
    enabled = BooleanField(lazy_gettext('Repo Enabled'))
    remote_url = StringField(lazy_gettext('Repo URL'), widget=BS3TextFieldWidget(), validators=[DataRequired()])
    remote_branch = StringField(lazy_gettext('Repo Branch'), widget=BS3TextFieldWidget(), validators=[DataRequired()])
    remote_user = StringField(lazy_gettext('Repo Username'), widget=BS3TextFieldWidget(), validators=[Optional()])
    remote_pass = PasswordField(lazy_gettext('Repo Password'), widget=BS3PasswordFieldWidget(), validators=[Optional()])
    interval = IntegerField(lazy_gettext('Refresh Interval'), widget=BS3TextFieldWidget(),
                            validators=[NumberRange(min=0)])


class DAGRepoView(ModelView):
    route_base = "/repo"
    datamodel = SQLAInterface(DAGRepo)

    base_permissions = ['can_add', 'can_list', 'can_edit', 'can_delete']
    base_order = ('name', 'asc')

    label_columns = {'name': 'Repo Name', 'enabled': 'Repo Enabled', 'remote_url': 'Remote URL',
                     'remote_branch': 'Remote Branch', 'interval': 'Refresh (Seconds)', 'last_updated': 'Last Updated'}

    search_columns = ['name', 'enabled', 'remote_url', 'remote_branch', 'last_updated']
    list_columns = ['name', 'enabled', 'remote_url', 'remote_branch', 'interval', 'last_updated']

    add_columns = edit_columns = ['name', 'enabled', 'remote_url', 'remote_branch', 'remote_user',
                                  'remote_pass', 'interval']

    show_columns = edit_columns.copy()
    show_columns.append('last_updated')

    add_form = edit_form = DAGRepoForm
