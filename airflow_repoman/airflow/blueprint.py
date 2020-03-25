from airflow import settings
from flask import Blueprint, Flask, request, Response

from airflow_repoman.common.models import DAGRepo

repoman_blueprint = Blueprint('repo_bp', __name__, url_prefix="/repo")


def check_auth(username, password):
    ses = settings.Session()
    userobj = ses.query(DAGRepo).filter((DAGRepo.remote_user == username) & DAGRepo.push_only)
    if userobj.count() == 1:
        userobj: DAGRepo = userobj.one()
        if userobj.remote_pass == password:
            return True
        else:
            return False
    else:
        return None


def test_auth(u, p):
    print("{} : {}".format(u, p))
    return True


@repoman_blueprint.route('/test', methods=['GET', 'POST'])
def test():
    if request.authorization is None:
        resp = Response("REQ LOGIN")
        resp.status_code = 401
        resp.headers['WWW-Authenticate'] = "Basic realm=repoman"
        return resp
    else:
        username = request.authorization.get('username')
        password = request.authorization.get('password')

        if test_auth(username, password):
            if request.method == 'POST':
                print(request.files)
                print(request.data)
                return ""
            else:
                return "REQUIRES POST METHOD", 405
        else:
            return "LOGIN INVALID", 403


if __name__ == "__main__":
    app = Flask(__name__)
    app.debug = True
    app.register_blueprint(repoman_blueprint)
    app.run('0.0.0.0', 8888)
