from flask import Flask, request, jsonify
import os

from models import app, db, ma

# import models
from models.StellarSystemModel import StellarSystem, StellarSystemSchema

# Init schemas
stellar_system_schema = StellarSystemSchema()
stellar_systems_schema = StellarSystemSchema(many=True)

# routes
@app.route('/stellarsystems', methods=['GET'])
def get_stellar_systems():
    all_stellar_systems = StellarSystem.query.all()
    result = stellar_system_schema.dump(all_stellar_systems)
    return jsonify(result.data)

@app.route('/stellarsystem', methods=['POST'])
def add_stellar_system():


    return jsonify({ "Hello": "World!"})



# run.py
if __name__ == '__main__':
    app.run(debug=True)