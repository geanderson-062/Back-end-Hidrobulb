from fastapi import APIRouter
import random

router = APIRouter()


@router.get("/time_interval/")
def get_time_interval():
    time_interval = random.randint(1, 24)
    return {"time_interval": time_interval}
