from pydantic import BaseModel


class TimeInterval(BaseModel):
    time_interval: str
