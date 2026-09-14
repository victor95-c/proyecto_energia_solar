from ejecuciones import (
    ejecutar_bridge,
    ejecutar_composite,
    ejecutar_decorator,
    ejecutar_prototype,
    ejecutar_singleton
)


def ejecutar_patrones():
    print("\n")
    print("========================================")
    print("     SISTEMA DE ENERGÍA SOLAR")
    print("========================================")

    ejecutar_singleton()
    ejecutar_prototype()
    potencia = ejecutar_composite()
    ejecutar_decorator(potencia)
    ejecutar_bridge()

    print("\n========================================")
    print("       PROGRAMA FINALIZADO")
    print("========================================")


if __name__ == "__main__":
    ejecutar_patrones()
