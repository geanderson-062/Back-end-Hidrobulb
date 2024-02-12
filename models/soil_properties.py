from pydantic import BaseModel


class SoilProperties(BaseModel):
    soil_texture: str
    hydraulic_conductivity: float
    porosity: float
    field_capacity: float
    wilting_point: float
