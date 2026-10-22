# =====================================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: [Tu Nombre], [Nombre Integrante 2], [Nombre Integrante 3]
# Fecha: 14/10/2026 | Versión: 1.0
# Descripción: Verifica combustible y aplica condicional simple de advertencia.
# =====================================================================

RESERVA_EMERGENCIA = 10

comb_disponible = int(input("Combustible disponible: "))
comb_ida = int(input("Combustible para ida: "))
comb_regreso = int(input("Combustible para regreso: "))

comb_total = comb_ida + comb_regreso + RESERVA_EMERGENCIA
comb_adicional = comb_disponible - comb_total

print("\n--- ESTADO DE COMBUSTIBLE ---")
print("Combustible disponible:", comb_disponible)
print("Requerido para llegar:", comb_ida)
print("Requerido para regresar:", comb_regreso)
print("Reserva de emergencia:", RESERVA_EMERGENCIA)
print("Combustible total requerido:", comb_total)
print("Combustible adicional disponible:", comb_adicional)

# Regla de advertencia mediante condicional simple
if comb_adicional < 10:
    print("Advertencia: el margen adicional de combustible es bajo.")