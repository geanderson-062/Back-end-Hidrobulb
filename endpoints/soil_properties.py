from fastapi import APIRouter
from services.soil_properties import (
    generate_soil_properties_norte,
    generate_soil_properties_nordeste,
    generate_soil_properties_centro_oeste,
    generate_soil_properties_sudeste,
    generate_soil_properties_sul,
)

from models.soil_properties import SoilProperties

router = APIRouter()


@router.get(
    "/soil_properties/norte",
    response_model=SoilProperties,
    tags=["Soil Properties"],
    summary="Get Soil Properties",
)
def get_soil_properties():
    return generate_soil_properties_norte()


@router.get(
    "/soil_properties/nordeste",
    response_model=SoilProperties,
    tags=["Soil Properties"],
    summary="Get Soil Properties",
)
def get_soil_properties():
    return generate_soil_properties_nordeste()


@router.get(
    "/soil_properties/centro_oeste",
    response_model=SoilProperties,
    tags=["Soil Properties"],
    summary="Get Soil Properties",
)
def get_soil_properties():
    return generate_soil_properties_centro_oeste()


@router.get(
    "/soil_properties/sudeste",
    response_model=SoilProperties,
    tags=["Soil Properties"],
    summary="Get Soil Properties",
)
def get_soil_properties():
    return generate_soil_properties_sudeste()


@router.get(
    "/soil_properties/sul",
    response_model=SoilProperties,
    tags=["Soil Properties"],
    summary="Get Soil Properties",
)
def get_soil_properties():
    return generate_soil_properties_sul()
