from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class Area(db.Model):
    __tablename__ = 'area'
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    status_id = db.Column(db.Integer,nullable=False)
    plant_id = db.Column(db.Integer,nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<Area {self.area}>'

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class VisitLog(db.Model):
    __tablename__ = 'visit_logs'
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    route = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)