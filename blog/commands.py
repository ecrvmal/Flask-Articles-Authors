from wsgi import app
from blog.app import db
from models import User


@app.cli.command('init-db')
def init_db():
    db.create_all()
