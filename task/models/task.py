from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

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

    def to_dict(self):
        tmp_dict = {
            "id":self.id,
            "name":self.name,
            "status":self.status
        }
        return tmp_dict

    
    