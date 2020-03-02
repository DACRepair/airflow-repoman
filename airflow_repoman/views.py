from flask_appbuilder import BaseView, expose


class TestView(BaseView):
    @expose('/')
    def list(self):
        return "Potato"
