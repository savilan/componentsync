from w3admin import db

class Frecuency(db.Model):
    __tablename__ = 'frecuency'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    value = db.Column(db.Integer)

    def __repr__(self):
        return f'<Frecuency {self.name}>'