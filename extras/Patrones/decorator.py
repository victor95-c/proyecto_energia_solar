from abc import ABC, abstractmethod


class GeneracionSolar(ABC):

    @abstractmethod
    def calcular(self):
        pass


class GeneracionBase(GeneracionSolar):
    """
    Generación básica:

    Energía = Potencia × Horas de sol
    """

    def __init__(self, potencia, horas_sol):
        self.potencia = potencia
        self.horas_sol = horas_sol

    def calcular(self):
        return self.potencia * self.horas_sol


class GeneracionDecorator(GeneracionSolar):

    def __init__(self, generacion):
        self.generacion = generacion

    def calcular(self):
        return self.generacion.calcular()


class PerdidasDecorator(GeneracionDecorator):

    def __init__(
        self,
        generacion,
        porcentaje
    ):
        super().__init__(generacion)
        self.porcentaje = porcentaje

    def calcular(self):

        energia = self.generacion.calcular()

        perdida = energia * (
            self.porcentaje / 100
        )

        return energia - perdida

class EficienciaDecorator(GeneracionDecorator):

    def __init__(
        self,
        generacion,
        eficiencia
    ):
        super().__init__(generacion)
        self.eficiencia = eficiencia

    def calcular(self):

        energia = self.generacion.calcular()

        return energia * (
            self.eficiencia / 100
        )

class TemperaturaDecorator(GeneracionDecorator):

    def __init__(
        self,
        generacion,
        temperatura
    ):
        super().__init__(generacion)
        self.temperatura = temperatura

    def calcular(self):

        energia = self.generacion.calcular()

        if self.temperatura > 25:

            grados_extra = (
                self.temperatura - 25
            )

            perdida = grados_extra * 0.4

            energia *= (
                1 - perdida / 100
            )

        return energia