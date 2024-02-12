from fastapi import APIRouter
from pydantic import BaseModel
import random

router = APIRouter()


class BoundaryConditions(BaseModel):
    surface_water_flow: float
    evaporation_rate: float
    precipitation: float


@router.get("/boundary_conditions/", response_model=BoundaryConditions)
def get_boundary_conditions():
    surface_water_flow = round(random.uniform(0, 10), 2)
    evaporation_rate = round(random.uniform(0, 5), 2)
    precipitation = round(random.uniform(0, 20), 2)
    return {
        "surface_water_flow": surface_water_flow,
        "evaporation_rate": evaporation_rate,
        "precipitation": precipitation,
    }
