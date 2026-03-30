"""
Módulo con funciones para la validación de direcciones de email.
Ejercicio 4 - Actividad 2 Python UNLP 2026.
"""


def validar_email(email: str) -> bool:
    """
    Valida una dirección de email según criterios básicos.

    Criterios:
        - Contiene exactamente un @.
        - No empieza ni termina con @ ni con .
        - Tiene al menos un carácter antes y después del @.
        - El dominio contiene al menos un punto.
        - La parte después del último punto tiene al menos 2 caracteres.

    Args:
        email: Dirección de email a validar.

    Returns:
        True si el email es válido, False en caso contrario.
    """
    if email.count('@') != 1:
        return False

    if email.startswith('@') or email.startswith('.'):
        return False

    if email.endswith('@') or email.endswith('.'):
        return False

    partes = email.split('@')
    if len(partes[0]) == 0 or len(partes[1]) == 0:
        return False

    dominio = partes[1].split('.')
    if len(dominio) < 2 or len(dominio[-1]) < 2:
        return False

    return True