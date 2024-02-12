import random
from models.time_interval import TimeInterval


def generate_time_interval():
    time_interval = random.randint(1, 24)
    return TimeInterval(time_interval=str(time_interval))
