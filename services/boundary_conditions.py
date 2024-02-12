import random
from models.boundary_conditions import BoundaryConditions


def generate_boundary_conditions_norte():
    mean_surface_water_flow = 7
    std_dev_surface_water_flow = 2
    mean_evaporation_rate = 3
    std_dev_evaporation_rate = 1
    mean_precipitation = 15
    std_dev_precipitation = 5

    surface_water_flow = max(
        0, round(random.gauss(mean_surface_water_flow, std_dev_surface_water_flow), 2)
    )
    evaporation_rate = max(
        0, round(random.gauss(mean_evaporation_rate, std_dev_evaporation_rate), 2)
    )
    precipitation = max(
        0, round(random.gauss(mean_precipitation, std_dev_precipitation), 2)
    )

    return BoundaryConditions(
        surface_water_flow=surface_water_flow,
        evaporation_rate=evaporation_rate,
        precipitation=precipitation,
    )


def generate_boundary_conditions_nordeste():
    mean_surface_water_flow = 6
    std_dev_surface_water_flow = 2
    mean_evaporation_rate = 3
    std_dev_evaporation_rate = 1
    mean_precipitation = 20
    std_dev_precipitation = 5

    surface_water_flow = max(
        0, round(random.gauss(mean_surface_water_flow, std_dev_surface_water_flow), 2)
    )
    evaporation_rate = max(
        0, round(random.gauss(mean_evaporation_rate, std_dev_evaporation_rate), 2)
    )
    precipitation = max(
        0, round(random.gauss(mean_precipitation, std_dev_precipitation), 2)
    )

    return BoundaryConditions(
        surface_water_flow=surface_water_flow,
        evaporation_rate=evaporation_rate,
        precipitation=precipitation,
    )


def generate_boundary_conditions_centro_oeste():
    mean_surface_water_flow = 8
    std_dev_surface_water_flow = 2
    mean_evaporation_rate = 2.5
    std_dev_evaporation_rate = 1
    mean_precipitation = 10
    std_dev_precipitation = 5

    surface_water_flow = max(
        0, round(random.gauss(mean_surface_water_flow, std_dev_surface_water_flow), 2)
    )
    evaporation_rate = max(
        0, round(random.gauss(mean_evaporation_rate, std_dev_evaporation_rate), 2)
    )
    precipitation = max(
        0, round(random.gauss(mean_precipitation, std_dev_precipitation), 2)
    )

    return BoundaryConditions(
        surface_water_flow=surface_water_flow,
        evaporation_rate=evaporation_rate,
        precipitation=precipitation,
    )


def generate_boundary_conditions_sudeste():
    mean_surface_water_flow = 5
    std_dev_surface_water_flow = 2
    mean_evaporation_rate = 2.5
    std_dev_evaporation_rate = 1
    mean_precipitation = 15
    std_dev_precipitation = 5

    surface_water_flow = max(
        0, round(random.gauss(mean_surface_water_flow, std_dev_surface_water_flow), 2)
    )
    evaporation_rate = max(
        0, round(random.gauss(mean_evaporation_rate, std_dev_evaporation_rate), 2)
    )
    precipitation = max(
        0, round(random.gauss(mean_precipitation, std_dev_precipitation), 2)
    )

    return BoundaryConditions(
        surface_water_flow=surface_water_flow,
        evaporation_rate=evaporation_rate,
        precipitation=precipitation,
    )


def generate_boundary_conditions_sul():
    mean_surface_water_flow = 4
    std_dev_surface_water_flow = 1.5
    mean_evaporation_rate = 2
    std_dev_evaporation_rate = 0.5
    mean_precipitation = 20
    std_dev_precipitation = 5

    surface_water_flow = max(
        0, round(random.gauss(mean_surface_water_flow, std_dev_surface_water_flow), 2)
    )
    evaporation_rate = max(
        0, round(random.gauss(mean_evaporation_rate, std_dev_evaporation_rate), 2)
    )
    precipitation = max(
        0, round(random.gauss(mean_precipitation, std_dev_precipitation), 2)
    )

    return BoundaryConditions(
        surface_water_flow=surface_water_flow,
        evaporation_rate=evaporation_rate,
        precipitation=precipitation,
    )
