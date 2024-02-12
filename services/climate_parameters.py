import random
from models.climate_parameters import ClimateParameters


def generate_climate_parameters_norte():
    temperature = max(0, round(random.gauss(30, 3), 2))
    humidity = max(0, round(random.gauss(75, 5), 2))
    wind_speed = max(0, round(random.gauss(3, 1), 2))
    radiation = max(0, round(random.gauss(500, 100), 2))
    return ClimateParameters(
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed,
        radiation=radiation,
    )


def generate_climate_parameters_nordeste():
    temperature = max(0, round(random.gauss(32, 3), 2))
    humidity = max(0, round(random.gauss(70, 5), 2))
    wind_speed = max(0, round(random.gauss(4, 1), 2))
    radiation = max(0, round(random.gauss(650, 100), 2))
    return ClimateParameters(
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed,
        radiation=radiation,
    )


def generate_climate_parameters_centro_oeste():
    temperature = max(0, round(random.gauss(28, 3), 2))
    humidity = max(0, round(random.gauss(60, 5), 2))
    wind_speed = max(0, round(random.gauss(3.5, 1), 2))
    radiation = max(0, round(random.gauss(550, 100), 2))
    return ClimateParameters(
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed,
        radiation=radiation,
    )


def generate_climate_parameters_sudeste():
    temperature = max(0, round(random.gauss(25, 3), 2))
    humidity = max(0, round(random.gauss(65, 5), 2))
    wind_speed = max(0, round(random.gauss(3, 1), 2))
    radiation = max(0, round(random.gauss(450, 100), 2))
    return ClimateParameters(
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed,
        radiation=radiation,
    )


def generate_climate_parameters_sul():
    temperature = max(0, round(random.gauss(20, 3), 2))
    humidity = max(0, round(random.gauss(70, 5), 2))
    wind_speed = max(0, round(random.gauss(3, 1), 2))
    radiation = max(0, round(random.gauss(350, 100), 2))
    return ClimateParameters(
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed,
        radiation=radiation,
    )
