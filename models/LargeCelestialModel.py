import os
import datetime

from . import db, ma


class LargeCelestial(db.Model):
    __tablename__ = 'large_celestial'

    id = db.Column(db.Integer, primary_key=True)
    stellar_system_id = db.Column(db.Integer, db.ForeignKey('stellar_system.id'), nullable=False)
    smallCelestials = db.relationship('SmallCelestial', backref='large_celestial', lazy=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, name, stellar_system_id):
        self.name = name
        self.stellar_system_id = stellar_system_id
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()


class LargeCelestialSchema(ma.Schema):
    class Meta:
        fields = ('id', 'stellar_system_id', 'small_celestials','name', 'created_at', 'modified_at')
