from fastapi import APIRouter
from services.soil_properties import generate_soil_properties
from models.soil_properties import SoilProperties

router = APIRouter()


@router.get(
    "/soil_properties/",
    response_model=SoilProperties,
    tags=["Soil Properties"],
    summary="Get Soil Properties",
)
def get_soil_properties():
    return generate_soil_properties()
