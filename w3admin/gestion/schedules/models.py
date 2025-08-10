from datetime import datetime
from w3admin import db

class Schedule(db.Model):
    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    start_day = db.Column(db.Date, nullable=False)
    start_datetime = db.Column(db.Time, nullable=False)
    end_day = db.Column(db.Date, nullable=False)
    end_datetime = db.Column(db.Time, nullable=False)
    status_id = db.Column(db.Integer, nullable=False)
    condition_id = db.Column(db.Integer, nullable=False)
    frecuency_id = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
