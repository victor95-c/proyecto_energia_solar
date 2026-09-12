import requests

from fastapi import APIRouter

from API.solar_api import SolarAPIService


router = APIRouter()
solar_api = SolarAPIService()


@router.get("/api/info")
def inicio():
    return {
        "mensaje": "API de energia solar activa",
        "documentacion": "/docs",
    }


@router.get("/estado")
def estado_sistema():
    return {"estado": "Sistema de energia solar activo"}


@router.get("/datos")
def datos_solares(latitud: float = 11.2408, longitud: float = -74.1990):
    datos = solar_api.obtener_datos(latitud, longitud)
    horario = datos["hourly"]

    return {
        "latitud": latitud,
        "longitud": longitud,
        "radiacion_w_m2": horario["shortwave_radiation"][0],
        "temperatura_c": horario["temperature_2m"][0],
    }


@router.get("/ubicacion")
def ubicacion_coordenadas(
    latitud: float = 11.2408,
    longitud: float = -74.1990,
):
    try:
        respuesta = requests.get(
            "https://nominatim.openstreetmap.org/reverse",
            params={
                "lat": latitud,
                "lon": longitud,
                "format": "jsonv2",
                "zoom": 10,
                "addressdetails": 1,
            },
            headers={"User-Agent": "SolarPro/1.0"},
            timeout=10,
        )
        respuesta.raise_for_status()
        direccion = respuesta.json().get("address", {})
        ciudad = (
            direccion.get("city")
            or direccion.get("town")
            or direccion.get("municipality")
            or direccion.get("village")
            or "Ubicación sin ciudad"
        )
        region = direccion.get("state") or direccion.get("county") or ""
        pais = direccion.get("country") or ""
        return {
            "nombre": ", ".join(
                parte for parte in (ciudad, region, pais) if parte
            ),
            "latitud": latitud,
            "longitud": longitud,
        }
    except requests.RequestException:
        return {
            "nombre": f"Coordenadas: {latitud:.4f}, {longitud:.4f}",
            "latitud": latitud,
            "longitud": longitud,
        }

