from fastapi import APIRouter
from . import (
    soil_properties,
    initial_conditions,
    boundary_conditions,
    climate_parameters,
    domain_geometry,
    time_interval,
    saturation_drainage,
)

router = APIRouter()


@router.get("/all_parameters/")
def get_all_parameters():
    soil_props = soil_properties.get_soil_properties()
    initial_conds = initial_conditions.get_initial_conditions()
    boundary_conds = boundary_conditions.get_boundary_conditions()
    climate_params = climate_parameters.get_climate_parameters()
    domain_geom = domain_geometry.get_domain_geometry()
    time_int = time_interval.get_time_interval()
    saturation_drain = saturation_drainage.get_saturation_drainage()

    all_params = {
        "soil_properties": soil_props,
        "initial_conditions": initial_conds,
        "boundary_conditions": boundary_conds,
        "climate_parameters": climate_params,
        "domain_geometry": domain_geom,
        "time_interval": time_int,
        "saturation_drainage": saturation_drain,
    }

    return all_params
