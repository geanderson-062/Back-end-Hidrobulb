from fastapi import APIRouter
from services.saturation_drainage import generate_saturation_drainage
from models.saturation_drainage import SaturationDrainage

router = APIRouter()


@router.get("/saturation_drainage/", response_model=SaturationDrainage)
def get_saturation_drainage():
    return generate_saturation_drainage()
