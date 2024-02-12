from fastapi import APIRouter
from pydantic import BaseModel
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


class AllParameters(BaseModel):
    soil_texture: str
    hydraulic_conductivity: float
    porosity: float
    field_capacity: float
    wilting_point: float
    initial_moisture: float
    solute_concentration: float
    surface_water_flow: float
    evaporation_rate: float
    precipitation: float
    temperature: float
    humidity: float
    wind_speed: float
    radiation: float
    soil_thickness: float
    surface_area: float
    time_interval: str
    saturation: str
    drainage: str


@router.get("/all_parameters/", response_model=AllParameters)
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
