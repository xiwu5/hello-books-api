from flask.cli import FlaskGroup
from app import create_app
from app.db import db

cli = FlaskGroup(create_app=create_app)

if __name__ == '__main__':
    db.create_all()
    cli()