"""
Módulo con funciones para el análisis estadístico de textos.
Ejercicio 1 -  Python UNLP 2026.
"""



def palabras_por_linea(lineas: list, palabras: list) -> float:
    """
    Calcula el promedio de palabras por línea.
    
    Args:
        lineas: Lista de líneas del texto.
        palabras: Lista de todas las palabras del texto.
    
    Returns:
        Promedio de palabras por línea como float.
    """
    return len(palabras) / len(lineas)


def lineas_sobre_promedio(lineas: list, prom: float) -> list:
    """
    Devuelve las líneas cuya cantidad de palabras supera el promedio.
    
    Args:
        lineas: Lista de líneas del texto.
        prom: Promedio de palabras por línea.
    
    Returns:
        Lista de líneas que superan el promedio.
    """
    sobre_promedio = []
    for linea in lineas:
        if len(linea.split()) > prom:
            sobre_promedio.append(linea)
    return sobre_promedio
