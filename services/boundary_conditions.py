import random
from models.boundary_conditions import BoundaryConditions


def generate_boundary_conditions():
    surface_water_flow = round(random.uniform(0, 10), 2)
    evaporation_rate = round(random.uniform(0, 5), 2)
    precipitation = round(random.uniform(0, 20), 2)
    return BoundaryConditions(
        surface_water_flow=surface_water_flow,
        evaporation_rate=evaporation_rate,
        precipitation=precipitation,
    )
