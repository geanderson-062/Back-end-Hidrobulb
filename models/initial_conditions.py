from pydantic import BaseModel


class InitialConditions(BaseModel):
    initial_moisture: float
    solute_concentration: float
