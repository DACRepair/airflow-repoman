from flask_admin.contrib.sqla import ModelView
# from flask_admin.form import SecureForm
from wtforms.fields import PasswordField


class DAGRepoAdminView(ModelView):
    # form_base_class = SecureForm
    can_view_details = True

    column_searchable_list = ['name', 'enabled', 'remote_url', 'remote_branch', 'last_updated']
    column_list = ['name', 'enabled', 'remote_url', 'remote_branch', 'interval', 'last_updated']

    form_excluded_columns = ['id', 'last_checked', 'last_updated']
    form_overrides = {'remote_pass': PasswordField}
