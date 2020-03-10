from flask_admin.contrib.sqla import ModelView
from wtforms.fields import PasswordField


class DAGRepoAdminView(ModelView):
    can_view_details = True
    column_details_exclude_list = ['id', 'remote_pass']

    column_searchable_list = ['name', 'enabled', 'remote_url', 'remote_branch', 'last_updated']
    column_list = ['name', 'enabled', 'remote_url', 'remote_branch', 'interval', 'last_updated']

    form_excluded_columns = ['id', 'last_checked', 'last_updated']
    form_overrides = {'remote_pass': PasswordField}
