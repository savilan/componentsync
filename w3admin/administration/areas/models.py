from datetime import datetime
from w3admin import db

class Area(db.Model):
    __tablename__ = 'area'
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    status_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<Area {self.area}>'