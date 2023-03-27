from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')
# the Blueprint will be registered in app.py
# when request  localhost/users   > goes to the Bluepront (url_prefix param)
# when request  localhost/users   > goes to function under @user.route('/')

USERS = {1: 'Alice', 2: 'John', 3: 'Mike'}


@user.route('/')
def user_list():
    return render_template(
        'users/list.html',
        users=USERS,
    )



@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        # raise NotFound(f'user id {pk} not found')      # change error message
        return redirect('/users/')                       # or make action  (redirect) on error
    return render_template(
        'users/details.html',
        user_name=user_name,     # possible to pass any variables. objects
    )