
from flask import Flask

from blog import commands
from blog.extensions import db, login_manager, migrate, csrf
from blog.models import User
from blog.admin import admin
from blog.api import init_api


def create_app() -> Flask:

    """
    The create_app function is the application factory.
    It takes as an argument the name of a configuration to be used for the app.
    The config object from that module or class is then used to configure your Flask app.

    :return: A flask object
    """
    app = Flask(__name__)
    app.config.from_object('blog.config')

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    # register_api(app)
    # register_api_routes()
    return app


def register_extensions(app):

    """
    The register_extensions function is responsible for initializing all of the Flask extensions that we will be using in our application.

    :param app: Pass the flask app instance to the function
    :return: The api object
    """
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True, render_as_batch=True)
    csrf.init_app(app)

    # api.plugins = [
    #     ApiSpecPlugin(
    #         app=app,
    #         tags={
    #             'Tag': 'Tag API',
    #             # 'User': 'User API',
    #             # 'Author': 'Author API',
    #             # 'Article': 'Article API',
    #         }
    #     ),
    # ]
    api = init_api(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


# def register_api(app: Flask):
#     from blog.api.tag import TagList
#     from blog.api.tag import TagDetail
#     api.init_app(app)
#     api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
#     api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>', tag='Tag')



# def register_api_routes():
#     from blog.api.tag import TagList
#     from blog.api.tag import TagDetail
    # from blog.api.user import UserList
    # from blog.api.user import UserDetail
    # from blog.api.author import AuthorList
    # from blog.api.author import AuthorDetail
    # from blog.api.article import ArticleList
    # from blog.api.article import ArticleDetail

    # api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
    # api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>', tag='Tag')

    # api.route(UserList, 'user_list', '/api/users/', tag='User')
    # api.route(UserDetail, 'user_detail', '/api/users/<int:id>', tag='User')
    #
    # api.route(AuthorList, 'author_list', '/api/authors/', tag='Author')
    # api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>', tag='Author')
    #
    # api.route(ArticleList, 'article_list', '/api/articles/', tag='Article')
    # api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>', tag='Article')


def register_blueprints(app: Flask):

    """
    The register_blueprints function is a helper function that allows us to register all of our blueprints in one place.
    This makes it easier for us to keep track of the blueprints we have registered and where they are located.

    :param app: Flask: Pass the flask application object to the function
    :return: None
    """
    from blog.auth.view import auth
    from blog.user.views import user
    from blog.report.views import report
    from blog.author.views import author
    from blog.articles.views import article

    app.register_blueprint(user)
    app.register_blueprint(auth)
    app.register_blueprint(report)
    app.register_blueprint(author)
    app.register_blueprint(article)

    admin.init_app(app)


def register_commands(app: Flask):

    # the there is migrations, the init-db don't need
    # app.cli.add_command(commands.init_db)
    """
    The register_commands function registers the CLI commands with Flask.

    :param app: Flask: Register the commands with the flask app
    :return: None
    """
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.create_user)
    app.cli.add_command(commands.create_init_tags)

