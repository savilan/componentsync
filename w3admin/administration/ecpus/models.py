from w3admin import db

class ECPU(db.Model):
    __tablename__ = 'ecpu'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), nullable=False)
    node = db.Column(db.String(4), nullable=False)
    name = db.Column(db.String(25), nullable=False)
    descrip = db.Column(db.String(100), nullable=False)
    status_id = db.Column(db.Integer, nullable=False)
    e_inventory_id = db.Column(db.Integer)

    def __repr__(self):
        return f'<ECPU {self.name}>'