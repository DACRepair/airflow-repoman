from flask_admin.contrib.sqla import ModelView


class DAGRepoAdminView(ModelView):
    column_searchable_list = ['name', 'enabled', 'remote_url', 'remote_branch', 'last_updated']
    column_list = ['name', 'enabled', 'remote_url', 'remote_branch', 'interval', 'last_updated']
