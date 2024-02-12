from fastapi import APIRouter
from services.climate_parameters import (
    generate_climate_parameters_norte,
    generate_climate_parameters_nordeste,
    generate_climate_parameters_centro_oeste,
    generate_climate_parameters_sudeste,
    generate_climate_parameters_sul,
)
from models.climate_parameters import ClimateParameters

router = APIRouter()


@router.get(
    "/climate_parameters/norte",
    response_model=ClimateParameters,
    tags=["Climate Parameters"],
    summary="Get Climate Parameters Norte",
)
def get_climate_parameters():
    return generate_climate_parameters_norte()


@router.get(
    "/climate_parameters/nordeste",
    response_model=ClimateParameters,
    tags=["Climate Parameters"],
    summary="Get Climate Parameters Nordeste",
)
def get_climate_parameters():
    return generate_climate_parameters_nordeste()


@router.get(
    "/climate_parameters/centro_oeste",
    response_model=ClimateParameters,
    tags=["Climate Parameters"],
    summary="Get Climate Parameters Centro Oeste",
)
def get_climate_parameters():
    return generate_climate_parameters_centro_oeste()


@router.get(
    "/climate_parameters/sudeste",
    response_model=ClimateParameters,
    tags=["Climate Parameters"],
    summary="Get Climate Parameters Sudeste",
)
def get_climate_parameters():
    return generate_climate_parameters_sudeste()


@router.get(
    "/climate_parameters/sul",
    response_model=ClimateParameters,
    tags=["Climate Parameters"],
    summary="Get Climate Parameters Sul",
)
def get_climate_parameters():
    return generate_climate_parameters_sul()
