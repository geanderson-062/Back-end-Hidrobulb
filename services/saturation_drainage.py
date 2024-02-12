import random
from models.saturation_drainage import SaturationDrainage


def generate_saturation_drainage_norte():
    saturation = random.choice(["Saturated", "Unsaturated"])
    drainage = random.choice(["Free drainage", "Restricted drainage"])
    return SaturationDrainage(saturation=saturation, drainage=drainage)


def generate_saturation_drainage_nordeste():
    saturation = random.choice(["Saturated", "Unsaturated"])
    drainage = random.choice(["Free drainage", "Restricted drainage"])
    return SaturationDrainage(saturation=saturation, drainage=drainage)


def generate_saturation_drainage_centro_oeste():
    saturation = random.choice(["Saturated", "Unsaturated"])
    drainage = random.choice(["Free drainage", "Restricted drainage"])
    return SaturationDrainage(saturation=saturation, drainage=drainage)


def generate_saturation_drainage_sudeste():
    saturation = random.choice(["Saturated", "Unsaturated"])
    drainage = random.choice(["Free drainage", "Restricted drainage"])
    return SaturationDrainage(saturation=saturation, drainage=drainage)


def generate_saturation_drainage_sul():
    saturation = random.choice(["Saturated", "Unsaturated"])
    drainage = random.choice(["Free drainage", "Restricted drainage"])
    return SaturationDrainage(saturation=saturation, drainage=drainage)
