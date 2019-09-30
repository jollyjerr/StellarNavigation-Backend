from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import os

# import calculation functions
from calculations.organize import formatToCytoscape

# config debug
logging.basicConfig(level=logging.DEBUG)

# import models
from models.SmallCelestialModel import SmallCelestial, SmallCelestialSchema
from models.LargeCelestialModel import LargeCelestial, LargeCelestialSchema
from models.StellarSystemModel import StellarSystem, StellarSystemSchema

# Init schemas
stellar_system_schema = StellarSystemSchema()
stellar_systems_schema = StellarSystemSchema(many=True)
small_celestial_schema = SmallCelestialSchema
small_celestials_schema = SmallCelestialSchema(many=True)

#import functional app
from models import app, db, ma
CORS(app)

# routes
@app.route('/stellarsystems', methods=['GET'])
def get_stellar_systems():
    all_stellar_systems = StellarSystem.query.all()
    result = stellar_systems_schema.dump(all_stellar_systems)
    return jsonify({"systems": result})

@app.route('/stellarsystem/<id>', methods=['GET'])
def get_stellar_system(id):
    stellar_system = StellarSystem.query.get(id)

    nodeList = []

    for key in stellar_system.largeCelestials:
        nodeList.append(formatToCytoscape(key))

    return jsonify(nodeList)





# run
if __name__ == '__main__':
    app.run(debug=True)
