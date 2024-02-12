from fastapi import APIRouter
from services.all_parameters import generate_all_parameters
from models.all_parameters import AllParameters

router = APIRouter()


@router.get("/all_parameters/", response_model=AllParameters)
def get_all_parameters():
    return generate_all_parameters()
