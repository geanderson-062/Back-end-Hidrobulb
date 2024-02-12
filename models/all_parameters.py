from pydantic import BaseModel


class AllParameters(BaseModel):
    soil_texture: str
    hydraulic_conductivity: float
    porosity: float
    field_capacity: float
    wilting_point: float
    initial_moisture: float
    solute_concentration: float
    surface_water_flow: float
    evaporation_rate: float
    precipitation: float
    temperature: float
    humidity: float
    wind_speed: float
    radiation: float
    soil_thickness: float
    surface_area: float
    time_interval: str
    saturation: str
    drainage: str
