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
    #STELLAR SYSTEMS
    # solar_system = StellarSystem(name="Solar System", stud="solar_system") 1st
    # solar_system = StellarSystem.query.filter_by(name="Solar System").first().id
    # alpha_centauri = StellarSystem(name="Alpha Centauri", stud="alpha_centauri")
    alpha_centauri = StellarSystem.query.filter_by(name="Alpha Centauri").first().id

    #LARGE CELESTIALS
    # sun = LargeCelestial(name="Sun", classification="body", radius=695510.0, orbital_period=82125000000.0, semi_major_axis=000.0, stellar_system=solar_system)   
    # mercury = LargeCelestial(name="Mercury", classification="body", radius=2439.7, orbital_period=88.0, semi_major_axis=57909050.0, stellar_system=solar_system)
    # venus = LargeCelestial(name="Venus", classification="body", radius=6051.8, orbital_period=255.0, semi_major_axis=108208000.0, stellar_system=solar_system)
    # earth = LargeCelestial(name="Earth", classification="body", radius=6356.0, orbital_period=365.0, semi_major_axis=149598023.0, stellar_system=solar_system)
    # mars = LargeCelestial(name="Mars", classification="body", radius=3389.5, orbital_period=687.0, semi_major_axis=227943771.6, stellar_system=solar_system)
    # jupiter = LargeCelestial(name="Jupiter", classification="body", radius=69911.0, orbital_period=4380.0, semi_major_axis=778570000.0, stellar_system=solar_system)
    # saturn = LargeCelestial(name="Saturn", classification="body", radius=58232.0, orbital_period=10585.0, semi_major_axis=1433530000.0, stellar_system=solar_system)
    # uranus = LargeCelestial(name="Uranus", classification="body", radius=25362.0, orbital_period=30660.0, semi_major_axis=2875031718.261, stellar_system=solar_system)
    # neptune = LargeCelestial(name="Neptune", classification="body", radius=24622.0, orbital_period=60225.0, semi_major_axis=4504390009.0, stellar_system=solar_system)

    # sun = LargeCelestial.query.filter_by(name="Sun").first().id  
    # mercury = LargeCelestial.query.filter_by(name="Mercury").first().id
    # venus = LargeCelestial.query.filter_by(name="Venus").first().id
    # earth = LargeCelestial.query.filter_by(name="Earth").first().id
    # mars = LargeCelestial.query.filter_by(name="Mars").first().id
    # jupiter = LargeCelestial.query.filter_by(name="Jupiter").first().id
    # saturn = LargeCelestial.query.filter_by(name="Saturn").first().id
    # uranus = LargeCelestial.query.filter_by(name="Uranus").first().id
    # neptune = LargeCelestial.query.filter_by(name="Neptune").first().id

    # alpha_centauri_A = LargeCelestial(name="Alpha Centauri A", classification="body", radius=851486.4, orbital_period=000.0, semi_major_axis=000.0, color='yellow', stellar_system_id=alpha_centauri)
    # alpha_centauri_B = LargeCelestial(name="Alpha Centauri B", classification="body", radius=600787.2, orbital_period=3.2357, semi_major_axis=598391500.0, color='red', stellar_system_id=alpha_centauri)
    # proxima_centauri_b = LargeCelestial(name="Proxima Centauri b", classification="body", radius=7356.0, orbital_period=11.186, semi_major_axis=733029500.7, color='green', stellar_system_id=alpha_centauri)
    proxima_centauri = LargeCelestial(name="Proxima Centauri", classification="body", radius=107276.94, orbital_period=199655000.0, semi_major_axis=130150000000.0, color='red', stellar_system_id=alpha_centauri)


    #SMALL CELESTIALS
    # moon = SmallCelestial(name="Moon", classification="body", radius=1737.1, orbital_period=27.3, semi_major_axis=379700.0, color='grey', stellar_system_id=solar_system, large_celestial_id=earth)
    # phobos = SmallCelestial(name="Phobos", classification="body", radius=11.267, orbital_period=0.33333333, semi_major_axis=9376, color='grey', stellar_system_id=solar_system, large_celestial_id=mars)
    # deimos = SmallCelestial(name="Deimos", classification="body", radius=6.2, orbital_period=0.792, semi_major_axis=23463.2, color='red', stellar_system_id=solar_system, large_celestial_id=mars)
    # vesta = SmallCelestial(name="Vesta", classification="body", radius=262.7, orbital_period=1325.654, semi_major_axis=353318755.0, color='silver', stellar_system_id=solar_system, large_celestial_id=sun)
    # juno = SmallCelestial(name="Juno", classification="body", radius=135.7, orbital_period=1592.86, semi_major_axis=399331484.679, color='grey', stellar_system_id=solar_system, large_celestial_id=sun)
    # ceres = SmallCelestial(name="Ceres", classification="body", radius=469.73, orbital_period=1683.145, semi_major_axis=413951699.542061, color='silver', stellar_system_id=solar_system, large_celestial_id=sun)
    # pallas = SmallCelestial(name="Pallas", classification="body", radius=272.5, orbital_period=1686, semi_major_axis=414523372.845154, color='blue', stellar_system_id=solar_system, large_celestial_id=sun)
    # lo = SmallCelestial(name="Lo", classification="body", radius=1821.6, orbital_period=1.769, semi_major_axis=421800.0, color='yellow', stellar_system_id=solar_system, large_celestial_id=jupiter)
    # europa = SmallCelestial(name="Europa", classification="body", radius=1560.8, orbital_period=3.551, semi_major_axis=671100.0, color='tan', stellar_system_id=solar_system, large_celestial_id=jupiter)
    # ganymede = SmallCelestial(name="Ganymede", classification="body", radius=2634.1, orbital_period=7.154, semi_major_axis=1070400.0, color='silver', stellar_system_id=solar_system, large_celestial_id=jupiter)
    # callisto = SmallCelestial(name="Callisto", classification="body", radius=2410.3, orbital_period=16.689, semi_major_axis=1882700.0, color='grey', stellar_system_id=solar_system, large_celestial_id=jupiter)
    # mimas = SmallCelestial(name="Mimas", classification="body", radius=198.2, orbital_period=0.942, semi_major_axis=185539.0, color='grey', stellar_system_id=solar_system, large_celestial_id=saturn)
    # enceladus = SmallCelestial(name="Enceladus", classification="body", radius=252.1, orbital_period=1.370, semi_major_axis=237958.0, color='silver', stellar_system_id=solar_system, large_celestial_id=saturn)
    # tethys = SmallCelestial(name="Tethys", classification="body", radius=531.1, orbital_period=1.887, semi_major_axis=294619.0, color='silver', stellar_system_id=solar_system, large_celestial_id=saturn)
    # dione = SmallCelestial(name="Dione", classification="body", radius=561.4, orbital_period=2.736, semi_major_axis=377369.0, color='grey', stellar_system_id=solar_system, large_celestial_id=saturn)
    # rhea = SmallCelestial(name="Rhea", classification="body", radius=763.8, orbital_period=4.518, semi_major_axis=527108.0, color='grey', stellar_system_id=solar_system, large_celestial_id=saturn)
    # titan = SmallCelestial(name="Titan", classification="body", radius=2574.73, orbital_period=15.945, semi_major_axis=1221870.0, color='yellow', stellar_system_id=solar_system, large_celestial_id=saturn)
    # miranda = SmallCelestial(name="Miranda", classification="body", radius=235.8, orbital_period=1.413, semi_major_axis=129390.0, color='silver', stellar_system_id=solar_system, large_celestial_id=uranus)
    # ariel = SmallCelestial(name="Ariel", classification="body", radius=578.9, orbital_period=2.52, semi_major_axis=191020.0, color='grey', stellar_system_id=solar_system, large_celestial_id=uranus)
    # umbriel = SmallCelestial(name="Umbriel", classification="body", radius=584.7, orbital_period=4.144, semi_major_axis=266000.0, color='grey', stellar_system_id=solar_system, large_celestial_id=uranus)
    # triton = SmallCelestial(name="Triton", classification="body", radius=1353.4, orbital_period=5.876, semi_major_axis=354759.0, color='silver', stellar_system_id=solar_system, large_celestial_id=neptune)
    # pluto = SmallCelestial(name="Pluto", classification="body", radius=1188.3, orbital_period=90560.2, semi_major_axis=590638000.0, color='pink', stellar_system_id=solar_system, large_celestial_id=sun)
    # charon = SmallCelestial(name="", classification="body", stellar_system_id=solar_system)
    # eris = SmallCelestial(name="", classification="body", stellar_system_id=solar_system)

    #DB ACTION
    # db.session.add(solar_system) 1st
    db.session.add_all([proxima_centauri])
    db.session.commit()


if __name__ == '__main__':
    manager.run()
