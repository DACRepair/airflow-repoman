from flask_appbuilder import BaseView, expose


class TestView(BaseView):
    @expose('/')
    def index(self):
        return "Potato"
