from fastapi import APIRouter
from pydantic import BaseModel
import random

router = APIRouter()


class TimeInterval(BaseModel):
    time_interval: str


@router.get("/time_interval/", response_model=TimeInterval)
def get_time_interval():
    time_interval = random.randint(1, 24)
    return {"time_interval": time_interval}
