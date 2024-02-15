import os
import requests
from fastapi import HTTPException


def get_info(role: str):
    routes = {
        "admin": "/all",
        "films": "/films",
        "people": "/people",
        "locations": "/locations",
        "species": "/species",
        "vehicles": "/vehicles"
    }

    if role not in routes:
        raise ValueError("Rol no válido")
    route = routes[role]
    api_url_base = os.getenv("API_URL")
    if api_url_base is None:
        raise ValueError("La variable de entorno API_URL no está definida")

    url = api_url_base + route
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=500, detail="Error al obtener datos de la API de Studio Ghibli")
