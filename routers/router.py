from fastapi import APIRouter
from endpoints import (
    soil_properties,
    initial_conditions,
    boundary_conditions,
    climate_parameters,
    domain_geometry,
    time_interval,
    saturation_drainage,
    all_parameters,
)

router = APIRouter()

router.include_router(soil_properties.router)
router.include_router(initial_conditions.router)
router.include_router(boundary_conditions.router)
router.include_router(climate_parameters.router)
router.include_router(domain_geometry.router)
router.include_router(time_interval.router)
router.include_router(saturation_drainage.router)
router.include_router(all_parameters.router)
