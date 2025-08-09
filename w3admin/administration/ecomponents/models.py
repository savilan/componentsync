from w3admin import db

class EComponent(db.Model):
    __tablename__ = 'ecomponent'
    id = db.Column(db.Integer, primary_key=True)
    node = db.Column(db.String(4), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    status_id = db.Column(db.Integer, nullable=False)
    ecpu_id = db.Column(db.Integer, nullable=False)
    frecuency_id = db.Column(db.Integer, nullable=False)
    value1 = db.Column(db.String(6))
    value2 = db.Column(db.String(6))
    value3 = db.Column(db.String(6))
    is_on = db.Column(db.Boolean)
    type_id = db.Column(db.Integer)
    goberned_by = db.Column(db.JSON)
    e_detail_id = db.Column(db.Integer)

    def __repr__(self):
        return f'<EComponent {self.name}>'