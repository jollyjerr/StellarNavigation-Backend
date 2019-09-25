from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# import models
from models.StellarSystemModel import StellarSystem, StellarSystemSchema

# app init
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Init schemas


# test route
@app.route('/', methods=['GET'])
def say_hi():
    return jsonify({ "Hello": "World!"})

# run.py
if __name__ == '__main__':
    app.run(debug=True)