# =====================================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: [Tu Nombre], [Nombre Integrante 2], [Nombre Integrante 3]
# Fecha: 14/10/2026 | Versión: 1.0
# Descripción: Validación general de autorización de lanzamiento.
# =====================================================================

RESERVA_EMERGENCIA = 10

# 1. Entrada de Datos
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para ida: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
energia_disponible = int(input("Energía disponible: "))
energia_requerida = int(input("Energía requerida: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# 2. Procesamiento
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_EMERGENCIA

# 3. Decisión Compuesta (Estructura condicional doble sin anidar)
condicion_combustible = combustible_disponible >= combustible_total_requerido
condicion_oxigeno = oxigeno_disponible >= oxigeno_requerido
condicion_energia = energia_disponible >= energia_requerida
condicion_provisiones = provisiones_disponibles >= provisiones_requeridas

if condicion_combustible and condicion_oxigeno and condicion_energia and condicion_provisiones:
    print("\nLanzamiento autorizado.")
else:
    print("\nLanzamiento no autorizado. La misión debe ser revisada.")