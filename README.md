
# Misión Órbita

## Descripción
Simulador básico de exploración espacial desarrollado en Python para el curso
Principios de Programación 1 (SOFT-01, sección SCV3) de la Universidad CENFOTEC.
El proyecto se construye en tres avances:

- **Avance 1 – Preparación de la misión:** cuatro algoritmos independientes
  (recursos necesarios, combustible, soporte de la tripulación y autorización
  de lanzamiento).
- **Avance 2 – Ejecución de la misión:** actividades de exploración científica
  (ejercicio 7) y evaluación del regreso y supervivencia de la tripulación
  (ejercicio 8).

## Integrantes
- Josue Monge Miranda

## Estructura del repositorio
```
mision-orbita/
├── README.md
├── avance1/
│   ├── ejercicio1_recursos.py
│   ├── ejercicio2_combustible.py
│   ├── ejercicio3_soporte_tripulacion.py
│   └── ejercicio4_autorizacion.py
├── avance2/
│   ├── ejercicio7_exploracion.py
│   └── ejercicio8_regreso.py
└── documentacion/
    ├── avance1.pdf
    ├── avance2.pdf
    ├── ejercicio7_exploracion.pdf
    └── ejercicio8_regreso.pdf
```

## Instrucciones de ejecución
Cada programa es independiente y se ejecuta desde la consola con Python 3:

```
python avance1/ejercicio1_recursos.py
python avance1/ejercicio2_combustible.py
python avance1/ejercicio3_soporte_tripulacion.py
python avance1/ejercicio4_autorizacion.py
python avance2/ejercicio7_exploracion.py
python avance2/ejercicio8_regreso.py
```

Todos los datos se ingresan por consola como números enteros positivos.
En el ejercicio 7 el menú se repite hasta elegir la opción 4 o hasta que una
actividad no pueda realizarse por falta de recursos.

## Convenciones y estilos
- Variables en snake_case, con nombres descriptivos y en minúscula.
- Constantes en MAYÚSCULAS con guion bajo, declaradas al inicio del archivo.
- Sin números mágicos dentro de las fórmulas ni de las condiciones.
- Indentación de 4 espacios y espacios alrededor de los operadores.
- Encabezado en cada archivo (archivo, curso, integrantes, fecha, versión y descripción).
- Un comentario antes de cada bloque lógico: constantes, entrada, procesamiento,
  decisión y salida; los comentarios explican el porqué de las decisiones.
- Mensajes de consola con sus unidades.
- Commits con mensajes que describen el cambio realizado.
