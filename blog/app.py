from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import logout_user, LoginManager


from blog.report.views import report
from blog.user.views import user
from blog.auth.view import auth
# from blog.config import Development


db = SQLAlchemy()
login_manager = LoginManager()


def create_app() -> Flask:
    app = Flask(__name__)
    # app.config.from_object(Development)
    # app.config.from_pyfile('config.py')
    app.config['SECRET_KEY'] = 'osk$nc3e-o#)(imn3@eufenq4zcbj-bh!j$r+=+r5k)plr69)r'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User, Article

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for("auth.login"))

    register_blueprint(app)
    return app


# after  the register blueprint  , the blueprint will be registered in app.instance
def register_blueprint(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(auth)
