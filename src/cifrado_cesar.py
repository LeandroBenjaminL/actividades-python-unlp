"""
Módulo con funciones para el cifrado César.
Ejercicio 8 - Actividad 2 Python UNLP 2026.
"""

import string

MINUS_LETTER = string.ascii_lowercase
MAYUS_LETTER = string.ascii_uppercase


def cesar(mensaje: list, desplazamiento: int, cifrar: bool) -> str:
    """
    Aplica el cifrado César a un mensaje, cifrando o descifrando según el parámetro.

    Los caracteres que no son letras (espacios, puntuación, números) se mantienen
    sin cambios. Preserva mayúsculas y minúsculas.

    Args:
        mensaje: Lista de caracteres del mensaje a procesar.
        desplazamiento: Cantidad de posiciones a desplazar en el alfabeto.
        cifrar: True para cifrar, False para descifrar.

    Returns:
        String con el mensaje cifrado o descifrado.
    """
    for i in range(len(mensaje)):
        if mensaje[i] in MINUS_LETTER or mensaje[i] in MAYUS_LETTER:
            # Preservar mayúsculas o minúsculas según la letra original
            alfabeto = MINUS_LETTER if mensaje[i] in MINUS_LETTER else MAYUS_LETTER
            pos = alfabeto.index(mensaje[i])
            # Sumar o restar el desplazamiento con módulo para que rote
            nueva_pos = (pos + desplazamiento) % 26 if cifrar else (pos - desplazamiento) % 26
            mensaje[i] = alfabeto[nueva_pos]

    return ''.join(mensaje)

    