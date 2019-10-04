from models.StellarSystemModel import StellarSystem, StellarSystemSchema
from models.LargeCelestialModel import LargeCelestial, LargeCelestialSchema
from models.SmallCelestialModel import SmallCelestial, SmallCelestialSchema

import logging
logging.basicConfig(level=logging.DEBUG)


def calculate_trip_requirements(destinations):

    # logging.debug(destinations)

    distances = []
    names = []

    for destination in destinations:
            distances.append(destination['semi_major_axis'])
            names.append(destination['name'])


    opt_distance = distances[0]

    for distance in distances:
        opt_distance -= distance

    opt_distance = (abs(opt_distance) / 149597870.69)

    time = (opt_distance / 7.21436)

    resp = {
        'distance': opt_distance,
        'names': names,
        'time': time
    }

    return resp




