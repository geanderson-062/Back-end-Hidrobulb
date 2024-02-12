from pydantic import BaseModel


class BoundaryConditions(BaseModel):
    surface_water_flow: float
    evaporation_rate: float
    precipitation: float
