import random
from models.all_parameters import AllParameters


def generate_all_parameters():
    surface_water_flow = round(random.uniform(0, 10), 2)
    evaporation_rate = round(random.uniform(0, 5), 2)
    precipitation = round(random.uniform(0, 20), 2)
    temperature = round(random.uniform(10, 30), 2)
    humidity = round(random.uniform(30, 80), 2)
    wind_speed = round(random.uniform(1, 10), 2)
    radiation = round(random.uniform(100, 1000), 2)
    soil_thickness = round(random.uniform(10, 100), 2)
    surface_area = round(random.uniform(100, 1000), 2)
    initial_moisture = round(random.uniform(0.1, 0.5), 2)
    solute_concentration = round(random.uniform(0, 100), 2)
    saturation = random.choice(["Saturated", "Unsaturated"])
    drainage = random.choice(["Free drainage", "Restricted drainage"])
    soil_texture = random.choice(["Argiloso", "Arenoso", "Silte", "Franco"])
    hydraulic_conductivity = round(random.uniform(0.01, 10), 2)
    porosity = round(random.uniform(0.2, 0.6), 2)
    field_capacity = round(random.uniform(0.1, 0.4), 2)
    wilting_point = round(random.uniform(0.05, 0.2), 2)
    time_interval = random.randint(1, 24)
    return AllParameters(
        soil_texture=soil_texture,
        hydraulic_conductivity=hydraulic_conductivity,
        porosity=porosity,
        field_capacity=field_capacity,
        wilting_point=wilting_point,
        initial_moisture=initial_moisture,
        solute_concentration=solute_concentration,
        surface_water_flow=surface_water_flow,
        evaporation_rate=evaporation_rate,
        precipitation=precipitation,
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed,
        radiation=radiation,
        soil_thickness=soil_thickness,
        surface_area=surface_area,
        time_interval=time_interval,
        saturation=saturation,
        drainage=drainage,
    )
