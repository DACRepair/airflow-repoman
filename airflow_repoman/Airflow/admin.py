from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from flask_babel import lazy_gettext
from wtforms.fields import BooleanField, IntegerField, PasswordField, StringField


class DAGRepoAdminForm(SecureForm):
    name = StringField(lazy_gettext('Repo Name'))
    enabled = BooleanField(lazy_gettext('Repo Enabled'))
    remote_url = StringField(lazy_gettext('Repo URL'))
    remote_branch = StringField(lazy_gettext('Repo Branch'))
    remote_user = StringField(lazy_gettext('Repo Username'))
    remote_pass = PasswordField(lazy_gettext('Repo Password'))
    interval = IntegerField(lazy_gettext('Refresh Interval'))


class DAGRepoAdminView(ModelView):
    column_searchable_list = ['name', 'enabled', 'remote_url', 'remote_branch', 'last_updated']
    column_list = ['name', 'enabled', 'remote_url', 'remote_branch', 'interval', 'last_updated']
    form = DAGRepoAdminForm
