import click

from sayhello import app, db
from sayhello.models import Message


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop')
def init_db(drop):
    """Initialize the database."""
    if drop:
        click.confirm('Do you want to delete the database?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')

    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages. Default is 20.')
def generate_messages(count):
    """Generate fake messages."""
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()
    for i in range(count):
        message = Message(name=fake.name(),
                          content=fake.sentence(),
                          timestamp=fake.date_time_this_year()
                          )
        db.session.add(message)
    db.session.commit()
    click.echo('Fake messages have been generated.')
