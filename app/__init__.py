from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .config.config import config

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

    def __init__(self, name, status):
        self.name = name
        self.status = status

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app