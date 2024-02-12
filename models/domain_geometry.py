from pydantic import BaseModel


class DomainGeometry(BaseModel):
    soil_thickness: float
    surface_area: float
