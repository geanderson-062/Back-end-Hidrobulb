from fastapi import APIRouter
from pydantic import BaseModel
import random

router = APIRouter()


class SaturationDrainage(BaseModel):
    saturation: str
    drainage: str


@router.get("/saturation_drainage/", response_model=SaturationDrainage)
def get_saturation_drainage():
    saturation = random.choice(["Saturated", "Unsaturated"])
    drainage = random.choice(["Free drainage", "Restricted drainage"])
    return {"saturation": saturation, "drainage": drainage}
