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

class SistemaMonitoreado:
    """
    Bridge.

    Permite cambiar el tipo de monitor
    sin modificar el sistema.
    """

    def __init__(self, monitor):
        self.monitor = monitor

    def cambiar_monitor(self, monitor):
        self.monitor = monitor

    def mostrar_estado(self, mensaje):
        self.monitor.mostrar(mensaje)