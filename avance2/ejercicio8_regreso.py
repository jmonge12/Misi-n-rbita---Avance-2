# =====================================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: Josue Monge Miranda
# Fecha: 08/11/2026    Versión: 1.0
# Descripción: Evalúa si la nave puede iniciar el regreso. Si puede,
#              simula el viaje día por día; si no, calcula cuántos días
#              puede sobrevivir la tripulación varada.
# =====================================================================

# --- Declaración de constantes ---
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_DIA = 2        # por tripulante
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_DIA = 1    # por tripulante

# --- Entrada de datos ---
cantidad_tripulantes = int(input("Cantidad de tripulantes: "))
dias_ida = int(input("Días del viaje de ida: "))
combustible = int(input("Combustible disponible: "))
oxigeno = int(input("Oxígeno disponible: "))
energia = int(input("Energía disponible: "))
provisiones = int(input("Provisiones disponibles: "))

# --- Procesamiento ---
# El regreso dura lo mismo que la ida. Aquí no se suma la reserva de
# emergencia, tal como lo indica la consigna.
combustible_regreso = dias_ida * CONSUMO_COMBUSTIBLE_DIA
oxigeno_diario = cantidad_tripulantes * CONSUMO_OXIGENO_DIA
provisiones_diarias = cantidad_tripulantes * CONSUMO_PROVISIONES_DIA

# --- Decisión: caso A (inicia el regreso) o caso B (tripulación varada) ---
if combustible >= combustible_regreso:
    # --- Caso A: simulación del regreso ---
    dias_completados = 0
    puede_continuar = True

    # El ciclo termina cuando se completan los días de la ida o cuando
    # un recurso no alcanza para el día siguiente.
    while puede_continuar and dias_completados < dias_ida:
        # Se verifica antes de descontar para no consumir nada de un día
        # que no se puede completar.
        if (combustible >= CONSUMO_COMBUSTIBLE_DIA
                and oxigeno >= oxigeno_diario
                and energia >= CONSUMO_ENERGIA_DIA
                and provisiones >= provisiones_diarias):
            combustible = combustible - CONSUMO_COMBUSTIBLE_DIA
            oxigeno = oxigeno - oxigeno_diario
            energia = energia - CONSUMO_ENERGIA_DIA
            provisiones = provisiones - provisiones_diarias
            dias_completados = dias_completados + 1
            print("Día", dias_completados, "| Combustible:", combustible,
                  "| Oxígeno:", oxigeno, "| Energía:", energia,
                  "| Provisiones:", provisiones)
        else:
            puede_continuar = False

    # --- Salida del caso A ---
    if dias_completados == dias_ida:
        print("La tripulación regresó exitosamente a la Tierra.")
        print("Combustible restante:", combustible, "unidades")
        print("Oxígeno restante:", oxigeno, "unidades")
        print("Energía restante:", energia, "unidades")
        print("Provisiones restantes:", provisiones, "unidades")
    else:
        # El día que falló es el siguiente al último día completado.
        dia_interrumpido = dias_completados + 1
        print("El regreso se interrumpió en el día " + str(dia_interrumpido) + ".")
        # El combustible no se revisa aquí porque ya se comprobó que alcanza.
        if oxigeno < oxigeno_diario:
            print("Recurso insuficiente: oxígeno")
        if energia < CONSUMO_ENERGIA_DIA:
            print("Recurso insuficiente: energía")
        if provisiones < provisiones_diarias:
            print("Recurso insuficiente: provisiones")
        print("La tripulación no completó el regreso.")
else:
    # --- Caso B: tripulación varada ---
    print("La tripulación quedó varada en el destino.")

    # División entera: solo cuentan los días completos.
    dias_oxigeno = oxigeno // oxigeno_diario
    dias_energia = energia // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones // provisiones_diarias

    # El mínimo se obtiene con condicionales, como lo pide la consigna.
    supervivencia_estimada = dias_oxigeno
    if dias_energia < supervivencia_estimada:
        supervivencia_estimada = dias_energia
    if dias_provisiones < supervivencia_estimada:
        supervivencia_estimada = dias_provisiones

    # Si hay empate, se agregan todos los recursos con el valor mínimo,
    # siempre en el orden oxígeno, energía y provisiones.
    recursos_limitantes = ""
    if dias_oxigeno == supervivencia_estimada:
        recursos_limitantes = "oxígeno"
    if dias_energia == supervivencia_estimada:
        if recursos_limitantes == "":
            recursos_limitantes = "energía"
        else:
            recursos_limitantes = recursos_limitantes + ", energía"
    if dias_provisiones == supervivencia_estimada:
        if recursos_limitantes == "":
            recursos_limitantes = "provisiones"
        else:
            recursos_limitantes = recursos_limitantes + ", provisiones"

    # --- Salida del caso B ---
    print("Días por oxígeno:", dias_oxigeno)
    print("Días por energía:", dias_energia)
    print("Días por provisiones:", dias_provisiones)
    print("Supervivencia estimada:", supervivencia_estimada, "días")
    print("Recurso(s) limitante(s):", recursos_limitantes)
