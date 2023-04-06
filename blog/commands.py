import click
from werkzeug.security import generate_password_hash
from blog.extensions import db



# the there is migrations, the init-db don't need
# @app.cli.command('init-db')
# def init_db():
#     db.create_all()


@click.command('create-init-user')
def create_init_user():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(email='name@example.com', password=generate_password_hash('test123'))
        )
        db.session.commit()


@click.command('create-user')
def create_user():
    from wsgi import app
    from blog.models import User

    with app.app_context():
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



