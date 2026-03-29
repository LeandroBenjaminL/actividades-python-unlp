"""
Módulo con funciones para el análisis de una playlist de canciones.
Ejercicio 2 - Actividad 2 Python UNLP 2026.
"""

def tot_duration (songs: list)-> str:
    """
    Calcula la duración total de la playlist.

    Args:
        songs: Lista de diccionarios con claves 'title' y 'duration' (formato 'm:ss').

    Returns:
        String con la duración total en formato 'Xm Ys'.
    """
    seg_total = 0
    for song in songs: 
        partes = song['duration'].split(':')
        seg_total += int(partes[0]) * 60 + int(partes[1])

    minute = seg_total // 60 
    seg = seg_total % 60
    return f'Duración total: {minute}m  {seg}s'
        



def long_song (songs: list) -> str:
    """
    Encuentra la canción más larga de la playlist.

    Args:
        songs: Lista de diccionarios con claves 'title' y 'duration' (formato 'm:ss').

    Returns:
        String con el título y duración de la canción más larga.
    """
    max_seg = 0
    for song in songs:
        partes = song['duration'].split(':')
        total_seg = int(partes[0]) * 60 + int(partes[1]) 
        if total_seg > max_seg: 
            max_seg = total_seg
            song_long = f'Canción más larga: "{song["title"]}" ({song["duration"]})'
    return song_long
                

def short_song (songs: list) -> str:
    """
    Encuentra la canción más corta de la playlist.

    Args:
        songs: Lista de diccionarios con claves 'title' y 'duration' (formato 'm:ss').

    Returns:
        String con el título y duración de la canción más corta.
    """
    min_seg = float('inf')
    for song in songs:
        partes = song['duration'].split(':')
        total_seg = int(partes[0]) * 60 + int(partes[1]) 
        if total_seg < min_seg: 
            min_seg = total_seg
            song_short = f'Canción más corta: "{song["title"]}" ({song["duration"]}) '
    return song_short



