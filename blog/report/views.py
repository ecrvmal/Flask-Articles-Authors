from flask import Blueprint

report = Blueprint('report', __name__, url_prefix='/reports', static_folder='../static')
# the Blueprint will be registered in app.py
# when request  localhost/users   > goes to the Bluepront (url_prefix param)
# when request  localhost/users   > goes to function under @user.route('/')


@report.route('/')
def report_list():
    return 'Hello_report'
