from abc import ABC, abstractmethod


class Monitor(ABC):
    """
    Implementación del Bridge.
    """

    @abstractmethod
    def mostrar(self, mensaje):
        pass

class MonitorConsola(Monitor):

    def mostrar(self, mensaje):
        print(f"[CONSOLA] {mensaje}")

class MonitorWeb(Monitor):

    def mostrar(self, mensaje):
        print(f"[WEB] {mensaje}")

class MonitorAPI(Monitor):

    def mostrar(self, mensaje):
        print(f"[API] {mensaje}")

class SistemaMonitoreado(ABC):
    """
    Abstracción del Bridge.
    Permite cambiar el tipo de monitor sin modificar el sistema.
    """

    def __init__(self, monitor: Monitor):
        self.monitor = monitor

    def cambiar_monitor(self, monitor: Monitor):
        self.monitor = monitor

    @abstractmethod
    def mostrar_estado(self, mensaje: str):
        pass

class SistemaResidencial(SistemaMonitoreado):
    def mostrar_estado(self, mensaje: str):
        # El sistema residencial formatea el mensaje de una manera simple
        mensaje_formateado = f"🏠 [Residencial] {mensaje}"
        self.monitor.mostrar(mensaje_formateado)

class SistemaComercial(SistemaMonitoreado):
    def mostrar_estado(self, mensaje: str):
        # El sistema comercial añade detalles técnicos o severidad
        mensaje_formateado = f"🏢 [Comercial] URGENTE: {mensaje}"
        self.monitor.mostrar(mensaje_formateado)