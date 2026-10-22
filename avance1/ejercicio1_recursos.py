# =====================================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: [Tu Nombre], [Nombre Integrante 2], [Nombre Integrante 3]
# Fecha: 14/10/2026 | Versión: 1.0
# Descripción: Calcula los recursos totales requeridos para una misión espacial.
# =====================================================================

# 1. Declaración de Constantes
CONSUMO_COMBUSTIBLE_DIA = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
EMERGENCIA_OXIGENO = 5
CONSUMO_ENERGIA_DIA = 5
EXPLORACION_ENERGIA = 10
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1
EXTRA_PROVISIONES = 3

# 2. Entrada de Datos
nombre_mision = input("Ingrese el nombre de la misión: ")
cantidad_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_estimados_ida = int(input("Ingrese los días estimados hasta el destino: "))

# 3. Procesamiento y Cálculos
combustible_ida = dias_estimados_ida * CONSUMO_COMBUSTIBLE_DIA
combustible_regreso = dias_estimados_ida * CONSUMO_COMBUSTIBLE_DIA
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

oxigeno_requerido = (dias_estimados_ida * CONSUMO_OXIGENO_TRIPULANTE_DIA * cantidad_tripulantes * 2) + EMERGENCIA_OXIGENO
energia_requerida = (dias_estimados_ida * CONSUMO_ENERGIA_DIA * 2) + EXPLORACION_ENERGIA
provisiones_requeridas = (dias_estimados_ida * CONSUMO_PROVISIONES_TRIPULANTE_DIA * cantidad_tripulantes * 2) + EXTRA_PROVISIONES

# 4. Salida de Resultados
print("\n--- RESUMEN DE RECURSOS REQUERIDOS ---")
print("Misión:", nombre_mision)
print("Tripulantes:", cantidad_tripulantes)
print("Duración estimada hasta el destino:", dias_estimados_ida, "dias")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxigeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")