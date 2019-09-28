import os
import datetime

from . import db, ma

from .SmallCelestialModel import SmallCelestialSchema

class LargeCelestial(db.Model):
    __tablename__ = 'large_celestial'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    classification = db.Column(db.String(10), nullable=False)
    radius = db.Column(db.Float, nullable=False)
    orbital_period = db.Column(db.Float, default=0)
    semi_major_axis = db.Column(db.Float, default=0)
    stellar_system_id = db.Column(db.Integer, db.ForeignKey('stellar_system.id'), nullable=False)
    smallCelestials = db.relationship('SmallCelestial', backref='large_celestial', lazy=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.name = data.get('name')
        self.classification = data.get('classification')
        self.radius = data.get('radius')
        self.orbital_period = data.get('orbital_period')
        self.semi_major_axis = data.get('semi_major_axis')
        self.stellar_system_id = data.get('stellar_system_id')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()


class LargeCelestialSchema(ma.ModelSchema):
    smallCelestials = ma.Nested(SmallCelestialSchema, many=True)
    class Meta:
        model = LargeCelestial
