import random
from models.initial_conditions import InitialConditions


def generate_initial_conditions():
    initial_moisture = round(random.uniform(0.1, 0.5), 2)
    solute_concentration = round(random.uniform(0, 100), 2)
    return InitialConditions(
        initial_moisture=initial_moisture, solute_concentration=solute_concentration
    )
