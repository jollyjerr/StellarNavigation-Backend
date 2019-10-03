from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import json
import os

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

# import calculation functions
from calculations.organize import formatToCytoscape
from calculations.trip_info import calculate_trip_requirements

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
        nodeList += formatToCytoscape(key)

    return jsonify(nodeList)

@app.route('/trip', methods=['POST'])
def calculate_trip():
    # data = json.load(request.json)
    
    return jsonify(calculate_trip_requirements(request.json))





# run
if __name__ == '__main__':
    app.run(debug=True)
