from flask import Blueprint, render_template

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')
# the Blueprint will be registered in app.py
# when request  localhost/users   > goes to the Bluepront (url_prefix param)
# when request  localhost/users   > goes to function under @user.route('/')

USERS = ['Alice', 'John', 'Mike']


@user.route('/')
def user_list():
    return render_template(
        'users/list.html',
        users=USERS,
    )



@user.route('/<pk>')
def get_user(pk: int):
    return pk
