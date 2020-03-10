from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from wtforms.fields import BooleanField, IntegerField, PasswordField, StringField


class DAGRepoAdminForm(SecureForm):
    name = StringField('Repo Name')
    enabled = BooleanField('Repo Enabled')
    remote_url = StringField('Repo URL')
    remote_branch = StringField('Repo Branch')
    remote_user = StringField('Repo Username')
    remote_pass = PasswordField('Repo Password')
    interval = IntegerField('Refresh Interval')


class DAGRepoAdminView(ModelView):
    column_searchable_list = ['name', 'enabled', 'remote_url', 'remote_branch', 'last_updated']
    column_list = ['name', 'enabled', 'remote_url', 'remote_branch', 'interval', 'last_updated']
    form = DAGRepoAdminForm
