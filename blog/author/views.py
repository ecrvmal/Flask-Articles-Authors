from flask_login import login_required
from flask import Blueprint, render_template

author = Blueprint('author', __name__, url_prefix='/authors', static_folder='../static')


@author.route('/')
# @login_required
def author_list():
    from blog.models import Author
    authors = Author.query.all()
    return render_template(
        'authors/list.html',
        authors=authors,
    )