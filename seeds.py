import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import db, app

migrate = Migrate(app, db)

manager = Manager(app)

from models.SmallCelestialModel import SmallCelestial, SmallCelestialSchema
from models.LargeCelestialModel import LargeCelestial, LargeCelestialSchema
from models.StellarSystemModel import StellarSystem, StellarSystemSchema


#Seeds
@manager.command
def seed():
    # solar_system = StellarSystem(name="Solar System")
    solar_system = StellarSystem.query.filter_by(name="Solar System").first().id

    # sun = LargeCelestial(name="Sun", classification="body", radius=695510.0, orbital_period=82125000000.0, semi_major_axis=000.0, stellar_system=solar_system)   
    # mercury = LargeCelestial(name="Mercury", classification="body", radius=2439.7, orbital_period=88.0, semi_major_axis=57909050.0, stellar_system=solar_system)
    # venus = LargeCelestial(name="Venus", classification="body", radius=6051.8, orbital_period=255.0, semi_major_axis=108208000.0, stellar_system=solar_system)
    # earth = LargeCelestial(name="Earth", classification="body", radius=6356.0, orbital_period=365.0, semi_major_axis=149598023.0, stellar_system=solar_system)
    # mars = LargeCelestial(name="Mars", classification="body", radius=3389.5, orbital_period=687.0, semi_major_axis=227943771.6, stellar_system=solar_system)
    # jupiter = LargeCelestial(name="Jupiter", classification="body", radius=69911.0, orbital_period=4380.0, semi_major_axis=778570000.0, stellar_system=solar_system)
    # saturn = LargeCelestial(name="Saturn", classification="body", radius=58232.0, orbital_period=10585.0, semi_major_axis=1433530000.0, stellar_system=solar_system)
    # uranus = LargeCelestial(name="Uranus", classification="body", radius=25362.0, orbital_period=30660.0, semi_major_axis=2875031718.261, stellar_system=solar_system)
    # neptune = LargeCelestial(name="Neptune", classification="body", radius=24622.0, orbital_period=60225.0, semi_major_axis=4504390009.0, stellar_system=solar_system)

    # db.session.add(solar_system)
    # db.session.add_all([sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune])

    


    db.session.commit()


if __name__ == '__main__':
    manager.run()
