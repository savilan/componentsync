from w3admin import db
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'es_CL.UTF-8')  # Asegura formato local

class VisitLog(db.Model):
    __tablename__ = 'visit_log'

    id = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.String(255))
    ip_address = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Propiedades para el template
    @property
    def dia(self):
        return self.created_at.strftime('%Y-%m-%d')

    @property
    def dia_semana(self):
        return self.created_at.strftime('%A').capitalize()

    @property
    def hora(self):
        return self.created_at.strftime('%H:%M:%S')
