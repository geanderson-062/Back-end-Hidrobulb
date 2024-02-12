from fastapi import APIRouter
from services.boundary_conditions import (
    generate_boundary_conditions_norte,
    generate_boundary_conditions_nordeste,
    generate_boundary_conditions_centro_oeste,
    generate_boundary_conditions_sudeste,
    generate_boundary_conditions_sul,
)
from models.boundary_conditions import BoundaryConditions

router = APIRouter()


@router.get(
    "/boundary_conditions/norte",
    response_model=BoundaryConditions,
    tags=["Boundary Conditions"],
    summary="Get Boundary Conditions Norte",
)
def get_boundary_conditions():
    return generate_boundary_conditions_norte()


@router.get(
    "/boundary_conditions/nordeste",
    response_model=BoundaryConditions,
    tags=["Boundary Conditions"],
    summary="Get Boundary Conditions Nordeste",
)
def get_boundary_conditions():
    return generate_boundary_conditions_nordeste()


@router.get(
    "/boundary_conditions/centro_oeste",
    response_model=BoundaryConditions,
    tags=["Boundary Conditions"],
    summary="Get Boundary Conditions Centro Oeste",
)
def get_boundary_conditions():
    return generate_boundary_conditions_centro_oeste()


@router.get(
    "/boundary_conditions/sudeste",
    response_model=BoundaryConditions,
    tags=["Boundary Conditions"],
    summary="Get Boundary Conditions Sudeste",
)
def get_boundary_conditions():
    return generate_boundary_conditions_sudeste()


@router.get(
    "/boundary_conditions/sul",
    response_model=BoundaryConditions,
    tags=["Boundary Conditions"],
    summary="Get Boundary Conditions Sul",
)
def get_boundary_conditions():
    return generate_boundary_conditions_sul()
