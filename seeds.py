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
    test_stellar_system = StellarSystem.query.filter_by(name="Bomba").first().id
    test_small = SmallCelestial("Little Fella", test_stellar_system)
    test_large = LargeCelestial("Big Fella", test_stellar_system)

    # db.session.add(test_stellar_system)
    db.session.add(test_small)
    db.session.add(test_large)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
