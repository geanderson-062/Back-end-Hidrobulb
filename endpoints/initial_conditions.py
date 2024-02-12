from fastapi import APIRouter
from services.initial_conditions import (
    generate_initial_conditions_norte,
    generate_initial_conditions_nordeste,
    generate_initial_conditions_centro_oeste,
    generate_initial_conditions_sudeste,
    generate_initial_conditions_sul,
)
from models.initial_conditions import InitialConditions

router = APIRouter()


@router.get(
    "/initial_conditions/norte",
    response_model=InitialConditions,
    tags=["Initial Conditions"],
    summary="Get Initial Conditions",
)
def get_initial_conditions():
    return generate_initial_conditions_norte()


@router.get(
    "/initial_conditions/nordeste",
    response_model=InitialConditions,
    tags=["Initial Conditions"],
    summary="Get Initial Conditions",
)
def get_initial_conditions():
    return generate_initial_conditions_nordeste()


@router.get(
    "/initial_conditions/centro_oeste",
    response_model=InitialConditions,
    tags=["Initial Conditions"],
    summary="Get Initial Conditions",
)
def get_initial_conditions():
    return generate_initial_conditions_centro_oeste()


@router.get(
    "/initial_conditions/sudeste",
    response_model=InitialConditions,
    tags=["Initial Conditions"],
    summary="Get Initial Conditions",
)
def get_initial_conditions():
    return generate_initial_conditions_sudeste()


@router.get(
    "/initial_conditions/sul",
    response_model=InitialConditions,
    tags=["Initial Conditions"],
    summary="Get Initial Conditions",
)
def get_initial_conditions():
    return generate_initial_conditions_sul()
