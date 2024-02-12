from pydantic import BaseModel


class SaturationDrainage(BaseModel):
    saturation: str
    drainage: str
