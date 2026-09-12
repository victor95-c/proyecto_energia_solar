import random

import requests

from Patrones.singleton import APIConfig


class SolarAPIService:

    def __init__(self):
        self.config = APIConfig()

    def obtener_datos(
        self,
        latitud,
        longitud
    ):

        parametros = {
            "latitude": latitud,
            "longitude": longitud,
            "hourly": (
                "shortwave_radiation,"
                "temperature_2m"
            ),
            "forecast_days": 1
        }

        respuesta = requests.get(
            self.config.api_url,
            params=parametros,
            timeout=10
        )

        respuesta.raise_for_status()

        datos = respuesta.json()
        cantidad_horas = len(
            datos["hourly"]["shortwave_radiation"]
        )
        datos["hourly"]["shortwave_radiation"] = [
            random.randint(0, 1000)
            for _ in range(cantidad_horas)
        ]

        return datos

    def obtener_radiacion(
        self,
        latitud,
        longitud
    ):

        datos = self.obtener_datos(
            latitud,
            longitud
        )

        return datos["hourly"][
            "shortwave_radiation"
        ]

    def obtener_temperatura(
        self,
        latitud,
        longitud
    ):

        datos = self.obtener_datos(
            latitud,
            longitud
        )

        return datos["hourly"][
            "temperature_2m"
        ]