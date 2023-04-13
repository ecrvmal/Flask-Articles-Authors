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
            User(username='user1', email='user1@mail.com',
                 first_name='user1', last_name='user1', birth_year=1991,
                 password=generate_password_hash('123'))
        )
        db.session.add(
            User(username='user2', email='user2@mail.com',
                 first_name='user2', last_name='user2', birth_year=1992,
                 password=generate_password_hash('123'))
        )
        db.session.add(
            User(username='user3', email='user3@mail.com',
                 first_name='user3', last_name='user3', birth_year=1993,
                 password=generate_password_hash('123'))
        )
        db.session.add(
            User(username='user4', email='user4@mail.com',
                 first_name='user4', last_name='user4', birth_year=1994,
                 password=generate_password_hash('123'))
        )
        db.session.add(
            User(username='user5', email='user5@mail.com',
                 first_name='user5', last_name='user5', birth_year=1995,
                 password=generate_password_hash('123'))
        )
        db.session.add(
            User(username='user6', email='username6@mail.com',
                 first_name='user6', last_name='user6', birth_year=1996,
                 password=generate_password_hash('123'))
        )
        db.session.commit()

@click.command('create-init-tags')
def create_init_tags():
    from blog.models import Tag
    from wsgi import app

    with app.app_context():
        tags = ('flask', 'django', 'python', 'gb', 'sqlite')
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo(f'Created tags : {", ".join(tags)}')






