import os
import datetime
from app import db, ma

class StellarSystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, name):
        self.name = name
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

class StellarSystemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'created_at', 'modified_at')