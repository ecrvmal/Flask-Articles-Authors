from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')
# the Blueprint will be registered in app.py
# when request  localhost/users   > goes to the Bluepront (url_prefix param)
# when request  localhost/users   > goes to function under @user.route('/')


@user.route('/')
def user_list():
    return 'Hello_user!'


@user.route('/<pk>')
def get_user(pk: int):
    return pk
