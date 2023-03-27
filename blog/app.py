from flask import Flask

from blog.report.views import report
from blog.user.views import user


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprint(app)
    return app


# after  the register blueprint  , the blueprint will be registered in app.instance
def register_blueprint(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)


