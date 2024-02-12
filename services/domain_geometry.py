import random
from models.domain_geometry import DomainGeometry


def generate_domain_geometry_norte():
    soil_thickness = max(0, round(random.gauss(100, 20), 2))
    surface_area = max(0, round(random.gauss(1000, 200), 2))
    return DomainGeometry(soil_thickness=soil_thickness, surface_area=surface_area)


def generate_domain_geometry_nordeste():
    soil_thickness = max(0, round(random.gauss(80, 15), 2))
    surface_area = max(0, round(random.gauss(800, 150), 2))
    return DomainGeometry(soil_thickness=soil_thickness, surface_area=surface_area)


def generate_domain_geometry_centro_oeste():
    soil_thickness = max(0, round(random.gauss(120, 25), 2))
    surface_area = max(0, round(random.gauss(1350, 250), 2))
    return DomainGeometry(soil_thickness=soil_thickness, surface_area=surface_area)


def generate_domain_geometry_sudeste():
    soil_thickness = max(0, round(random.gauss(60, 10), 2))
    surface_area = max(0, round(random.gauss(700, 100), 2))
    return DomainGeometry(soil_thickness=soil_thickness, surface_area=surface_area)


def generate_domain_geometry_sul():
    soil_thickness = max(0, round(random.gauss(80, 15), 2))
    surface_area = max(0, round(random.gauss(900, 150), 2))
    return DomainGeometry(soil_thickness=soil_thickness, surface_area=surface_area)
