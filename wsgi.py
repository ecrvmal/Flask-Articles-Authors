from blog.app import create_app
from blog.app import db
from werkzeug.security import generate_password_hash

app = create_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.cli.command('create-user')
def create_user():
    from blog.models import User
    db.session.add(
        User(username='user1', email='user1@mail.com', password=generate_password_hash('123'))
    )
    db.session.add(
        User(username='user2', email='user2@mail.com', password=generate_password_hash('123'))
    )
    db.session.add(
        User(username='user3', email='user3@mail.com', password=generate_password_hash('123'))
    )
    db.session.add(
        User(username='user4', email='user4@mail.com', password=generate_password_hash('123'))
    )
    db.session.add(
        User(username='user5', email='user5@mail.com', password=generate_password_hash('123'))
    )
    db.session.add(
        User(username='user6', email='username6@mail.com', password=generate_password_hash('123'))
    )
    db.session.commit()
