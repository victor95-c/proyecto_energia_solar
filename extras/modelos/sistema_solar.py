class SistemaSolarCompleto:

    def __init__(
        self,
        nombre,
        ubicacion,
        potencia
    ):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.potencia = potencia

    def mostrar(self):

        print("\n==============================")
        print(" INFORMACIÓN DEL SISTEMA")
        print("==============================")

        print(f"Nombre: {self.nombre}")
        print(f"Ubicación: {self.ubicacion}")
        print(
            f"Potencia instalada: "
            f"{self.potencia} W"
        )