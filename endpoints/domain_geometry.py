from fastapi import APIRouter
import random

router = APIRouter()


@router.get("/domain_geometry/")
def get_domain_geometry():
    soil_thickness = round(random.uniform(10, 100), 2)
    surface_area = round(random.uniform(100, 1000), 2)
    return {
        "soil_thickness": soil_thickness,
        "surface_area": surface_area,
    }
