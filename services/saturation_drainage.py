import random
from models.saturation_drainage import SaturationDrainage


def generate_saturation_drainage():
    saturation = random.choice(["Saturated", "Unsaturated"])
    drainage = random.choice(["Free drainage", "Restricted drainage"])
    return SaturationDrainage(saturation=saturation, drainage=drainage)
