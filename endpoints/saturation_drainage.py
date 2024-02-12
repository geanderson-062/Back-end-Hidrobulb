from fastapi import APIRouter
from models.saturation_drainage import SaturationDrainage
import random

router = APIRouter()


@router.get("/saturation_drainage/", response_model=SaturationDrainage)
def get_saturation_drainage():
    saturation = random.choice(["Saturated", "Unsaturated"])
    drainage = random.choice(["Free drainage", "Restricted drainage"])
    return {"saturation": saturation, "drainage": drainage}
