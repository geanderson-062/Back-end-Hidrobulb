from fastapi import APIRouter
from services.boundary_conditions import generate_boundary_conditions
from models.boundary_conditions import BoundaryConditions

router = APIRouter()


@router.get(
    "/boundary_conditions/",
    response_model=BoundaryConditions,
    tags=["Boundary Conditions"],
    summary="Get Boundary Conditions",
)
def get_boundary_conditions():
    return generate_boundary_conditions()
