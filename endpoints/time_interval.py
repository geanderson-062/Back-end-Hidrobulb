from fastapi import APIRouter
from services.time_interval import generate_time_interval
from models.time_interval import TimeInterval

router = APIRouter()


@router.get("/time_interval/", response_model=TimeInterval)
def get_time_interval():
    return generate_time_interval()
