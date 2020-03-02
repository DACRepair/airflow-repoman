from flask_appbuilder import BaseView, expose


class TestView(BaseView):
    default_view = "index"

    @expose('/')
    def index(self):
        return self.default_view
