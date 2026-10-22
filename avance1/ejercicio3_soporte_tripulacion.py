# =====================================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: [Tu Nombre], [Nombre Integrante 2], [Nombre Integrante 3]
# Fecha: 14/10/2026 | Versión: 1.0
# Descripción: Evalúa el soporte vital (oxígeno y provisiones) mediante condicional doble.
# =====================================================================

# 1. Entrada de Datos
oxigeno_disponible = int(input("Ingrese la cantidad de oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese la cantidad de oxígeno requerido: "))
provisiones_disponibles = int(input("Ingrese la cantidad de provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese la cantidad de provisiones requeridas: "))

# 2. Decisión y Salida (Estructura condicional doble sin anidar)
if (oxigeno_disponible >= oxigeno_requerido) and (provisiones_disponibles >= provisiones_requeridas):
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")