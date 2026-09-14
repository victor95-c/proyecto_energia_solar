from abc import ABC, abstractmethod


class ComponenteSolar(ABC):

    @abstractmethod
    def calcular_potencia(self):
        pass

    @abstractmethod
    def mostrar(self):
        pass
class PanelSolar(ComponenteSolar):
    """
    Hoja del patrón Composite.
    """
    def __init__(
        self,
        identificador,
        potencia,
        tipo
    ):
        self.identificador = identificador
        self.potencia = potencia
        self.tipo = tipo

    def calcular_potencia(self):
        return self.potencia

    def mostrar(self):
        return (
            f"Panel {self.identificador}: "
            f"{self.potencia} W - {self.tipo}"
        )


class ArregloSolar(ComponenteSolar):
    """
    Composite.

    Puede contener varios paneles.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def eliminar(self, componente):
        if componente in self.componentes:
            self.componentes.remove(componente)

    def calcular_potencia(self):

        total = 0

        for componente in self.componentes:
            total += componente.calcular_potencia()

        return total

    def mostrar(self):

        resultado = []

        resultado.append(
            f"\nArreglo: {self.nombre}"
        )

        for componente in self.componentes:
            resultado.append(
                componente.mostrar()
            )

        resultado.append(
            f"Potencia total: "
            f"{self.calcular_potencia()} W"
        )

        return "\n".join(resultado)