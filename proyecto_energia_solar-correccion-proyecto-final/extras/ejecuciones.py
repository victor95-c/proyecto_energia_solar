from API.solar_api import SolarAPIService
from Patrones.bridge import (
    MonitorConsola,
    MonitorWeb,
    SistemaResidencial
)
from Patrones.composite import (
    PanelSolar,
    ArregloSolar
)
from Patrones.decorator import (
    GeneracionBase,
    PerdidasDecorator,
    EficienciaDecorator,
    TemperaturaDecorator
)
from Patrones.prototype import SistemaSolar
from Patrones.singleton import APIConfig


def ejecutar_singleton():
    print("\n--- 1. SINGLETON ---")

    config1 = APIConfig()
    config2 = APIConfig()

    print("¿Las configuraciones son la misma instancia?")
    print(config1 is config2)
    print(config1.mostrar_configuracion())


def ejecutar_prototype():
    print("\n--- 2. PROTOTYPE ---")

    sistema_original = SistemaSolar(
        "Sistema Solar Principal",
        24,
        290,
        "Monocristalino",
        "Santa Marta"
    )
    sistema_clonado = sistema_original.clonar()
    sistema_clonado.nombre = "Sistema Solar Clonado"
    sistema_clonado.cantidad_paneles = 30

    print("\nSISTEMA ORIGINAL:")
    print(sistema_original.mostrar_informacion())
    print("\nSISTEMA CLONADO:")
    print(sistema_clonado.mostrar_informacion())


def ejecutar_composite():
    print("\n--- 3. COMPOSITE ---")

    arreglo = ArregloSolar("Arreglo Fotovoltaico")

    for identificador in range(1, 4):
        arreglo.agregar(
            PanelSolar(identificador, 290, "Monocristalino")
        )

    print(arreglo.mostrar())
    return arreglo.calcular_potencia()


def ejecutar_decorator(potencia):
    print("\n--- 4. DECORATOR ---")

    generacion = GeneracionBase(potencia, 5)
    print(f"Generación base: {generacion.calcular():.2f} Wh")

    generacion = PerdidasDecorator(generacion, 10)
    print(f"Con pérdidas: {generacion.calcular():.2f} Wh")

    generacion = EficienciaDecorator(generacion, 95)
    print(f"Con eficiencia: {generacion.calcular():.2f} Wh")

    generacion = TemperaturaDecorator(generacion, 30)
    print(f"Con temperatura: {generacion.calcular():.2f} Wh")


def ejecutar_bridge():
    print("\n--- 5. BRIDGE ---")

    sistema_monitoreado = SistemaResidencial(MonitorConsola())
    sistema_monitoreado.mostrar_estado(
        "Sistema funcionando correctamente"
    )

    print("\nCambiando monitor...")
    sistema_monitoreado.cambiar_monitor(MonitorWeb())
    sistema_monitoreado.mostrar_estado(
        "Generación enviada al monitor web"
    )


def ejecutar_api():
    print("\n--- 6. API SOLAR ---")

    api = SolarAPIService()
    latitud = 11.2408
    longitud = -74.1990

    try:
        radiacion = api.obtener_radiacion(latitud, longitud)
        temperatura = api.obtener_temperatura(latitud, longitud)

        print("\nDatos obtenidos correctamente.")
        print(f"Radiación solar: {radiacion[0]} W/m²")
        print(f"Temperatura: {temperatura[0]} °C")
    except Exception as error:
        print("\nNo se pudo consultar la API.")
        print(f"Error: {error}")
