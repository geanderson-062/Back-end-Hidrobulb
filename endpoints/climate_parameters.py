from fastapi import APIRouter
from pydantic import BaseModel
import random

router = APIRouter()


class ClimateParameters(BaseModel):
    temperature: float
    humidity: float
    wind_speed: float
    radiation: float


@router.get("/climate_parameters/", response_model=ClimateParameters)
def get_climate_parameters():
    temperature = round(random.uniform(10, 30), 2)
    humidity = round(random.uniform(30, 80), 2)
    wind_speed = round(random.uniform(1, 10), 2)
    radiation = round(random.uniform(100, 1000), 2)
    return {
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "radiation": radiation,
    }
