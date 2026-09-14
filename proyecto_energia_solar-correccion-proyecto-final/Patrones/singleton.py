class APIConfig:
    """
    Patrón Singleton.
    Solo puede existir una instancia de esta clase.
    """

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

            cls._instancia.api_url = (
                "https://api.open-meteo.com/v1/forecast"
            )

            cls._instancia.unidad_energia = "Wh"
            cls._instancia.unidad_temperatura = "°C"

        return cls._instancia

    def mostrar_configuracion(self):
        return {
            "API": self.api_url,
            "Energía": self.unidad_energia,
            "Temperatura": self.unidad_temperatura
        }