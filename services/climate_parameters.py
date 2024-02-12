import random
from models.climate_parameters import ClimateParameters


def generate_climate_parameters():
    temperature = round(random.uniform(10, 30), 2)
    humidity = round(random.uniform(30, 80), 2)
    wind_speed = round(random.uniform(1, 10), 2)
    radiation = round(random.uniform(100, 1000), 2)
    return ClimateParameters(
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed,
        radiation=radiation,
    )
