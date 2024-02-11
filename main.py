from fastapi import FastAPI
from typing import List
import random

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message": "Bem-vindo à API de simulação do comportamento do solo com o HYDRUS 3D. Consulte os endpoints específicos para obter dados sobre as propriedades do solo, condições iniciais, condições de contorno, parâmetros climáticos, geometria do domínio, intervalo de tempo e condições de saturação e drenagem."
    }


@app.get("/soil_properties/")
def get_soil_properties():
    soil_texture = random.choice(["Argiloso", "Arenoso", "Silte", "Franco"])
    hydraulic_conductivity = round(random.uniform(0.01, 10), 2)
    porosity = round(random.uniform(0.2, 0.6), 2)
    field_capacity = round(random.uniform(0.1, 0.4), 2)
    wilting_point = round(random.uniform(0.05, 0.2), 2)
    return {
        "texture": soil_texture,
        "hydraulic_conductivity": hydraulic_conductivity,
        "porosity": porosity,
        "field_capacity": field_capacity,
        "wilting_point": wilting_point,
    }


@app.get("/initial_conditions/")
def get_initial_conditions():
    initial_moisture = round(random.uniform(0.1, 0.5), 2)
    solute_concentration = round(random.uniform(0, 100), 2)
    return {
        "initial_moisture": initial_moisture,
        "solute_concentration": solute_concentration,
    }


@app.get("/boundary_conditions/")
def get_boundary_conditions():
    surface_water_flow = round(random.uniform(0, 10), 2)
    evaporation_rate = round(random.uniform(0, 5), 2)
    precipitation = round(random.uniform(0, 20), 2)
    return {
        "surface_water_flow": surface_water_flow,
        "evaporation_rate": evaporation_rate,
        "precipitation": precipitation,
    }


@app.get("/climate_parameters/")
def get_climate_parameters():
    temperature = round(random.uniform(10, 30), 2)
    humidity = round(random.uniform(30, 80), 2)
    wind_speed = round(random.uniform(1, 10), 2)
    radiation = round(random.uniform(100, 1000), 2)
    return {
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "radiation": radiation,
    }


@app.get("/domain_geometry/")
def get_domain_geometry():
    soil_thickness = round(random.uniform(10, 100), 2)
    surface_area = round(random.uniform(100, 1000), 2)
    return {
        "soil_thickness": soil_thickness,
        "surface_area": surface_area,
    }


@app.get("/time_interval/")
def get_time_interval():
    time_interval = random.randint(1, 24)
    return {"time_interval": time_interval}


@app.get("/saturation_drainage/")
def get_saturation_drainage():
    saturation = random.choice(["Saturated", "Unsaturated"])
    drainage = random.choice(["Free drainage", "Restricted drainage"])
    return {"saturation": saturation, "drainage": drainage}


@app.get("/all_parameters/")
def get_all_parameters():
    soil_properties = get_soil_properties()
    initial_conditions = get_initial_conditions()
    boundary_conditions = get_boundary_conditions()
    climate_parameters = get_climate_parameters()
    domain_geometry = get_domain_geometry()
    saturation_drainage = get_saturation_drainage()
    time_interval = get_time_interval()

    all_parameters = {
        "soil_properties": soil_properties,
        "initial_conditions": initial_conditions,
        "boundary_conditions": boundary_conditions,
        "climate_parameters": climate_parameters,
        "domain_geometry": domain_geometry,
        "saturation_drainage": saturation_drainage,
        "time_interval": time_interval,
    }

    return all_parameters
