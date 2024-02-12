from fastapi import APIRouter
from pydantic import BaseModel
import random

router = APIRouter()


class DomainGeometry(BaseModel):
    soil_thickness: float
    surface_area: float


@router.get("/domain_geometry/", response_model=DomainGeometry)
def get_domain_geometry():
    soil_thickness = round(random.uniform(10, 100), 2)
    surface_area = round(random.uniform(100, 1000), 2)
    return {
        "soil_thickness": soil_thickness,
        "surface_area": surface_area,
    }
