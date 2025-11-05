from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Use Flask-SQLAlchemy's default model class so the models register
# with the same metadata `db.create_all()` uses during tests.
db = SQLAlchemy()
migrate = Migrate()