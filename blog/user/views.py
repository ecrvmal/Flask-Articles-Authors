from flask import Blueprint, render_template, redirect
from flask_login import login_required
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')
# the Blueprint will be registered in app.py
# when request  localhost/users   > goes to the Bluepront (url_prefix param)
# when request  localhost/users   > goes to function under @user.route('/')

# USERS = {1: 'Alice', 2: 'John', 3: 'Mike'}


@user.route('/')
@login_required
def user_list():
    from blog.models import User
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )


@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    from blog.models import User

    _user = User.query.filter_by(id=pk).one_or_none()
    if not _user:
        raise NotFound(f'user id {pk} not found')      # change error message
        return redirect('/users/')                       # or make action  (redirect) on error
    return render_template(
        'users/profile.html',
        user=_user,     # possible to pass any variables. objects
    )