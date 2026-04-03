# Segundo Proyecto - Python UNLP 2026

Resolución de la Actividad 2 de la cursada de Python.

## Estructura del proyecto
```
Segundo Proyecto/
├── notebooks/      # Jupyter notebooks con los ejercicios
├── src/            # Código fuente con las funciones
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.x
- pip

## Instalación

1. Cloná el repositorio
2. Creá un entorno virtual:
```bash
   python -m venv .venv
```
3. Activá el entorno virtual:
```bash
   # Windows
   .venv\Scripts\activate

   # Mac/Linux
   source .venv/bin/activate
```
4. Instalá las dependencias:
```bash
   pip install -r requirements.txt
```

## Ejecución

1. Con el entorno activado, lanzá Jupyter:
```bash
   jupyter lab
```
2. Abrí la carpeta `notebooks/` y ejecutá los ejercicios.


## Ejercicios

### Ejercicio 1 - Estadísticas de un texto

Análisis del texto "El Zen de Python". Calcula:
- Total de líneas y palabras
- Promedio de palabras por línea
- Líneas que superan ese promedio

**Módulo:** `src/lines_calculate.py`  
**Notebook:** `notebooks/ejercicio1.ipynb`

### Ejercicio 2 - Duración de una playlist

Análisis de una playlist de canciones. Calcula:
- Duración total en formato `Xm Ys`
- Canción más larga y más corta

**Módulo:** `src/song_calculate.py`  
**Notebook:** `notebooks/02_Duración de una playlist.ipynb`

### Ejercicio 3 - Filtro de spoilers

Reemplaza palabras spoiler en una reseña de película por asteriscos
de la misma longitud, sin distinguir mayúsculas de minúsculas.

**Notebook:** `03_Filtro de spoilers.ipynb`

### Ejercicio 4 - Validación de email

Valida una dirección de email ingresada por el usuario
según criterios básicos de formato.

**Módulo:** `src/validation_email.py`
**Notebook:** `notebooks/04_Validación de email.ipynb`


### Ejercicio 5 - Calculadora de costo de envío

Calcula el costo de envío de un paquete según su peso y zona de destino.
Zonas válidas: local, regional, nacional.

**Módulo:** `src/kg_zona.py`  
**Notebook:** `notebooks/Calculadora de costo de envío.ipynb`

### Ejercicio 6 - Análisis de hashtags

Extrae hashtags de publicaciones, cuenta su frecuencia y muestra los trending.

**Notebook:** `notebooks/06_Analisis de hashtags.ipynb`