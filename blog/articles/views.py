from typing import Dict
import requests
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.orm import joinedload

from werkzeug.exceptions import NotFound

from blog.models import Article, Author, Tag
from blog.forms.article import CreateArticleForm
from blog.extensions import db

article = Blueprint('article', __name__, url_prefix='/article', static_folder='../static')


@article.route('/', methods=['GET'])
# @login_required
def article_list():
    """
    the function returns list of articles
    :return: to render template
    """
    from blog.models import Article
    articles = Article.query.all()
    # call RPC method
    count_articles_data: Dict = requests.get('http://127.0.0.1:5000/api/articles/event_get_count/').json()
    # {'count': 3, 'jsonapi': {'version': '1.0'}}
    count_articles = count_articles_data['count']
    # 3
    return render_template(
        'articles/list.html',
        articles=articles,
        count_articles=count_articles
    )


@article.route('/create', methods=['GET'])
@login_required
def create_article_form():
    """
    The create_article_form function renders the create.html template, which contains a form for creating an article.
    The form is populated with choices from the Tag table in the database.
    
    :return: The rendered template articles/create
    :doc-author: Trelent
    """
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    return render_template('articles/create.html', form=form)


@article.route('/create', methods=['POST'])
@login_required
def create_article():
    """
    The create_article function is responsible for creating a new article.
    It will first check if the user has submitted the form by checking if request.method == 'POST'.
    If it is, then we create an instance of CreateArticleForm and pass in request.form as its argument.
    We also set the choices attribute of our form to be a list of tuples containing all tags in our database ordered by name (line 4). This will allow us to use these tags when creating an article later on (see line 14). We then validate that this form was submitted correctly using WTForms' validate_on_submit method (line 5).

    :return: A redirect to the article detail page
    :doc-author: Trelent
    """
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)

        if current_user.author:
            _article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('article.article_detail', pk=_article.id))

    return render_template(
        'articles/create.html', form=form)


@article.route('/<int:pk>/', methods=['GET'])
# @login_required
def article_detail(pk):
    """
    The article_detail function is responsible for displaying a single article.
    It accepts an integer primary key (pk) as its only argument, and returns a
    response containing the rendered template 'articles/details.html'. The response
    contains the article object retrieved from the database using SQLAlchemy's query API.

    :param pk: Identify the article to be deleted
    :return: A rendered template
    :doc-author: Trelent
    """
    _article = Article.query.filter_by(id=pk).\
        options(joinedload(Article.tags)).\
        one_or_none()

    if _article is None:
        raise NotFound
    return render_template(
        'articles/details.html',
        article=_article,
    )
