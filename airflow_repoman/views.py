from flask_appbuilder import BaseView, expose


class TestView(BaseView):
    @expose('/')
    def list(self):
        return self.default_view
