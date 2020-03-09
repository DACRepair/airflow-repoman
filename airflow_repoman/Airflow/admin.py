from flask_admin.contrib.sqla import ModelView


class DAGRepoAdminView(ModelView):
    def __init__(self, model, session, name, category, *args, **kwargs):
        super(DAGRepoAdminView, self).__init__(model, session, name, category, *args, **kwargs)
