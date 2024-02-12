from fastapi import APIRouter
from models.time_interval import TimeInterval
import random

router = APIRouter()


@router.get("/time_interval/", response_model=TimeInterval)
def get_time_interval():
    time_interval = random.randint(1, 24)
    return {"time_interval": time_interval}
