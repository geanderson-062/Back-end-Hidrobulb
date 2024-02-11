from fastapi import APIRouter
import random

router = APIRouter()


@router.get("/saturation_drainage/")
def get_saturation_drainage():
    saturation = random.choice(["Saturated", "Unsaturated"])
    drainage = random.choice(["Free drainage", "Restricted drainage"])
    return {"saturation": saturation, "drainage": drainage}
