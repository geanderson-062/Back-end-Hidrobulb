from fastapi import APIRouter
from services.climate_parameters import generate_climate_parameters
from models.climate_parameters import ClimateParameters

router = APIRouter()


@router.get(
    "/climate_parameters/",
    response_model=ClimateParameters,
    tags=["Climate Parameters"],
    summary="Get Climate Parameters",
)
def get_climate_parameters():
    return generate_climate_parameters()
