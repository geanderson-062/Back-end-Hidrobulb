from fastapi import APIRouter
from services.initial_conditions import generate_initial_conditions
from models.initial_conditions import InitialConditions

router = APIRouter()


@router.get("/initial_conditions/", response_model=InitialConditions)
def get_initial_conditions():
    return generate_initial_conditions()
