import random
from models.soil_properties import SoilProperties


def generate_soil_properties_norte():
    soil_texture = random.choice(["Argiloso", "Arenoso", "Silte", "Franco"])
    hydraulic_conductivity = max(0, round(random.gauss(2.5, 1), 2))
    porosity = max(0, round(random.gauss(0.35, 0.05), 2))
    field_capacity = max(0, round(random.gauss(0.2, 0.05), 2))
    wilting_point = max(0, round(random.gauss(0.1, 0.03), 2))
    return SoilProperties(
        soil_texture=soil_texture,
        hydraulic_conductivity=hydraulic_conductivity,
        porosity=porosity,
        field_capacity=field_capacity,
        wilting_point=wilting_point,
    )


def generate_soil_properties_nordeste():
    soil_texture = random.choice(["Argiloso", "Arenoso", "Silte", "Franco"])
    hydraulic_conductivity = max(0, round(random.gauss(2.5, 1), 2))
    porosity = max(0, round(random.gauss(0.35, 0.05), 2))
    field_capacity = max(0, round(random.gauss(0.2, 0.05), 2))
    wilting_point = max(0, round(random.gauss(0.1, 0.03), 2))
    return SoilProperties(
        soil_texture=soil_texture,
        hydraulic_conductivity=hydraulic_conductivity,
        porosity=porosity,
        field_capacity=field_capacity,
        wilting_point=wilting_point,
    )


def generate_soil_properties_centro_oeste():
    soil_texture = random.choice(["Argiloso", "Arenoso", "Silte", "Franco"])
    hydraulic_conductivity = max(0, round(random.gauss(5, 2), 2))
    porosity = max(0, round(random.gauss(0.4, 0.1), 2))
    field_capacity = max(0, round(random.gauss(0.25, 0.05), 2))
    wilting_point = max(0, round(random.gauss(0.15, 0.03), 2))
    return SoilProperties(
        soil_texture=soil_texture,
        hydraulic_conductivity=hydraulic_conductivity,
        porosity=porosity,
        field_capacity=field_capacity,
        wilting_point=wilting_point,
    )


def generate_soil_properties_sudeste():
    soil_texture = random.choice(["Argiloso", "Arenoso", "Silte", "Franco"])
    hydraulic_conductivity = max(0, round(random.gauss(5, 2), 2))
    porosity = max(0, round(random.gauss(0.4, 0.1), 2))
    field_capacity = max(0, round(random.gauss(0.25, 0.05), 2))
    wilting_point = max(0, round(random.gauss(0.15, 0.03), 2))
    return SoilProperties(
        soil_texture=soil_texture,
        hydraulic_conductivity=hydraulic_conductivity,
        porosity=porosity,
        field_capacity=field_capacity,
        wilting_point=wilting_point,
    )


def generate_soil_properties_sul():
    soil_texture = random.choice(["Argiloso", "Arenoso", "Silte", "Franco"])
    hydraulic_conductivity = max(0, round(random.gauss(5, 2), 2))
    porosity = max(0, round(random.gauss(0.4, 0.1), 2))
    field_capacity = max(0, round(random.gauss(0.25, 0.05), 2))
    wilting_point = max(0, round(random.gauss(0.15, 0.03), 2))
    return SoilProperties(
        soil_texture=soil_texture,
        hydraulic_conductivity=hydraulic_conductivity,
        porosity=porosity,
        field_capacity=field_capacity,
        wilting_point=wilting_point,
    )
