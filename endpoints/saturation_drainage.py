from fastapi import APIRouter
from services.saturation_drainage import (
    generate_saturation_drainage_sul,
    generate_saturation_drainage_sudeste,
    generate_saturation_drainage_centro_oeste,
    generate_saturation_drainage_nordeste,
    generate_saturation_drainage_norte,
)
from models.saturation_drainage import SaturationDrainage

router = APIRouter()


@router.get(
    "/saturation_drainage/norte",
    response_model=SaturationDrainage,
    tags=["Saturation Drainage"],
    summary="Get Saturation Drainage Norte",
)
def get_saturation_drainage():
    return generate_saturation_drainage_norte()


@router.get(
    "/saturation_drainage/nordeste",
    response_model=SaturationDrainage,
    tags=["Saturation Drainage"],
    summary="Get Saturation Drainage Nordeste",
)
def get_saturation_drainage():
    return generate_saturation_drainage_nordeste()


@router.get(
    "/saturation_drainage/centro_oeste",
    response_model=SaturationDrainage,
    tags=["Saturation Drainage"],
    summary="Get Saturation Drainage Centro Oeste",
)
def get_saturation_drainage():
    return generate_saturation_drainage_centro_oeste()


@router.get(
    "/saturation_drainage/sudeste",
    response_model=SaturationDrainage,
    tags=["Saturation Drainage"],
    summary="Get Saturation Drainage Sudeste",
)
def get_saturation_drainage():
    return generate_saturation_drainage_sudeste()


@router.get(
    "/saturation_drainage/sul",
    response_model=SaturationDrainage,
    tags=["Saturation Drainage"],
    summary="Get Saturation Drainage Sul",
)
def get_saturation_drainage():
    return generate_saturation_drainage_sul()
