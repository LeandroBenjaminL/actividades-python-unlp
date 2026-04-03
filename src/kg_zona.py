"""
Módulo con funciones para el cálculo de costo de envío por peso y zona.
Ejercicio 5 - Actividad 2 Python UNLP 2026.
"""


def calcular_precio_kg(kg: float, precios: dict, z: str) -> int:
    """
    Calcula el costo de envío según el peso del paquete y la zona de destino.

    Args:
        kg: Peso del paquete en kilogramos.
        precios: Diccionario con los precios por rango de peso y zona.
        z: Zona de destino (local, regional o nacional).

    Returns:
        Costo de envío como entero, o -1 si la zona no es válida.
    """
    if z in precios['hasta_1kg']:
        if kg < 1:
            return precios['hasta_1kg'][z]
        elif kg < 5:
            return precios['entre_1_5kg'][z]
        else:
            return precios['mas_5kg'][z]
    return -1