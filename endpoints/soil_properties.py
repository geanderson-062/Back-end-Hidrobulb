from fastapi import APIRouter
from pydantic import BaseModel
import random

router = APIRouter()


class SoilProperties(BaseModel):
    soil_texture: str
    hydraulic_conductivity: float
    porosity: float
    field_capacity: float
    wilting_point: float


@router.get("/soil_properties/", response_model=SoilProperties)
def get_soil_properties():
    soil_texture = random.choice(["Argiloso", "Arenoso", "Silte", "Franco"])
    hydraulic_conductivity = round(random.uniform(0.01, 10), 2)
    porosity = round(random.uniform(0.2, 0.6), 2)
    field_capacity = round(random.uniform(0.1, 0.4), 2)
    wilting_point = round(random.uniform(0.05, 0.2), 2)
    return {
        "texture": soil_texture,
        "hydraulic_conductivity": hydraulic_conductivity,
        "porosity": porosity,
        "field_capacity": field_capacity,
        "wilting_point": wilting_point,
    }
