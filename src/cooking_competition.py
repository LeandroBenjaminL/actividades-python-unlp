"""
Módulo con funciones para la simulación de la competencia de cocina.
Ejercicio 10 - Actividad 2 Python UNLP 2026.
"""




def calcular_puntajes_ronda(scores: dict, stats: dict) -> dict:
    """
    Calcula el puntaje de cada participante en una ronda y actualiza
    sus estadísticas acumuladas. 

    Args:
        scores: Diccionario con los puntajes de cada juez por participante.
        stats: Diccionario con las estadísticas acumuladas de cada participante.

    Returns:
        Diccionario con el puntaje total de cada participante en la ronda.
    """
    puntajes_ronda = {}

    for participante in scores:
        puntaje = sum(scores[participante].values())
        puntajes_ronda[participante] = puntaje
        stats[participante]['total'] += puntaje
        if puntaje > stats[participante]['mejor_ronda']:
            stats[participante]['mejor_ronda'] = puntaje

    return puntajes_ronda

def imprimir_tabla_ronda(theme: str, ganador: str, puntajes_ronda: dict, stats: dict) -> None:
    """
    Imprime la tabla de posiciones de una ronda con el acumulado hasta el momento.

    Args:
        theme: Tema de la ronda.
        ganador: Nombre del ganador de la ronda.
        puntajes_ronda: Puntajes de cada participante en esta ronda.
        stats: Estadísticas acumuladas de cada participante.

    Returns:
        None. Solo imprime.
    """
    print(f'\nRonda - {theme}:')
    print(f'  Ganador: {ganador} ({puntajes_ronda[ganador]} pts)')
    print(f'  {"Cocinero":<15} {"Ronda":>6} {"Total":>6}')
    print(f'  {"-" * 30}')

    # Ordena por total acumulado de mayor a menor
    ordenado = sorted(stats.items(), key=lambda x: x[1]['total'], reverse=True) 
    # stats.items() te da pares de (nombre, diccionario)
    #  key=lambda x: x[1]['total'] por cada par, agarrá el segundo elemento x[1] (el diccionario) y compará por 'total'

    for participante, data in ordenado:
        print(f'  {participante:<15} {puntajes_ronda[participante]:>6} {data["total"]:>6}')


def imprimir_tabla_final(stats: dict, cant_rondas: int) -> None:
    """
    Imprime la tabla final de la competencia con estadísticas acumuladas.

    Args:
        stats: Diccionario con las estadísticas acumuladas de cada participante.
        cant_rondas: Cantidad total de rondas jugadas para calcular el promedio.

    Returns:
        None. Solo imprime.
    """
    print('\n' + '=' * 62)
    print('TABLA DE POSICIONES FINAL')
    print('=' * 62)
    print(f'  {"Cocinero":<15} {"Total":>6} {"Rondas gan.":>11} {"Mejor":>6} {"Promedio":>9}')
    print(f'  {"-" * 55}')

    ordenado = sorted(stats.items(), key=lambda x: x[1]['total'], reverse=True)

    for participante, data in ordenado:
        promedio = data['total'] / cant_rondas
        print(f'  {participante:<15} {data["total"]:>6} {data["rondas_ganadas"]:>11} {data["mejor_ronda"]:>6} {promedio:>9.1f}')

    print('=' * 62)
    print(f'  Total de rondas jugadas: {cant_rondas}')