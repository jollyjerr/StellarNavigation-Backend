import os
import datetime

from . import db, ma

from .LargeCelestialModel import LargeCelestialSchema
from .SmallCelestialModel import SmallCelestialSchema


class StellarSystem(db.Model):
    __tablename__ = 'stellar_system'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    largeCelestials = db.relationship('LargeCelestial', backref='stellar_system', lazy=True)
    smallCelestials = db.relationship('SmallCelestial', backref='stellar_system', lazy=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, name):
        self.name = name
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

class StellarSystemSchema(ma.ModelSchema):
    largeCelestials = ma.Nested(LargeCelestialSchema, many=True)
    smallCelestials = ma.Nested(SmallCelestialSchema, many=True)
    class Meta:
        model = StellarSystem
