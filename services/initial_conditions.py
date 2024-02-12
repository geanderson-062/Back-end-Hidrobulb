import random
from models.initial_conditions import InitialConditions


def generate_initial_conditions_norte():
    initial_moisture = max(0, round(random.gauss(0.4, 0.1), 2))
    solute_concentration = max(0, round(random.gauss(40, 10), 2))
    return InitialConditions(
        initial_moisture=initial_moisture, solute_concentration=solute_concentration
    )


def generate_initial_conditions_nordeste():
    initial_moisture = max(0, round(random.gauss(0.4, 0.1), 2))
    solute_concentration = max(0, round(random.gauss(40, 10), 2))
    return InitialConditions(
        initial_moisture=initial_moisture, solute_concentration=solute_concentration
    )


def generate_initial_conditions_centro_oeste():
    initial_moisture = max(0, round(random.gauss(0.4, 0.1), 2))
    solute_concentration = max(0, round(random.gauss(40, 10), 2))
    return InitialConditions(
        initial_moisture=initial_moisture, solute_concentration=solute_concentration
    )


def generate_initial_conditions_sudeste():
    initial_moisture = max(0, round(random.gauss(0.3, 0.1), 2))
    solute_concentration = max(0, round(random.gauss(50, 15), 2))
    return InitialConditions(
        initial_moisture=initial_moisture, solute_concentration=solute_concentration
    )


def generate_initial_conditions_sul():
    initial_moisture = max(0, round(random.gauss(0.3, 0.1), 2))
    solute_concentration = max(0, round(random.gauss(50, 15), 2))
    return InitialConditions(
        initial_moisture=initial_moisture, solute_concentration=solute_concentration
    )
