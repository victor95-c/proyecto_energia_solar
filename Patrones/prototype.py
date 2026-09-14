import copy


class SistemaSolar:
    """
    Patrón Prototype.
    Permite clonar un sistema solar existente.
    """

    def __init__(
        self,
        nombre,
        cantidad_paneles,
        potencia_panel,
        tipo_panel,
        ubicacion
    ):
        self.nombre = nombre
        self.cantidad_paneles = cantidad_paneles
        self.potencia_panel = potencia_panel
        self.tipo_panel = tipo_panel
        self.ubicacion = ubicacion

    def clonar(self):
        return copy.deepcopy(self)

    def calcular_potencia(self):
        return (
            self.cantidad_paneles
            * self.potencia_panel
        )

    def mostrar_informacion(self):

        return (
            f"Nombre: {self.nombre}\n"
            f"Paneles: {self.cantidad_paneles}\n"
            f"Potencia por panel: {self.potencia_panel} W\n"
            f"Tipo: {self.tipo_panel}\n"
            f"Ubicación: {self.ubicacion}\n"
            f"Potencia total: "
            f"{self.calcular_potencia()} W"
        )