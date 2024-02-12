from pydantic import BaseModel


class ClimateParameters(BaseModel):
    temperature: float
    humidity: float
    wind_speed: float
    radiation: float
