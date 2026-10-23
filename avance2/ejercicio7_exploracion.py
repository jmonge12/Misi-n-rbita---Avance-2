# =====================================================================
# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: Josue Monge Miranda
# Fecha: 08/11/2026    Versión: 1.0
# Descripción: Muestra un menú repetitivo de actividades de exploración
#              científica y acumula los puntos obtenidos.
# =====================================================================

# --- Declaración de constantes ---
# Las opciones y los costos van aquí para no dejar números mágicos
# dentro de las condiciones ni de las fórmulas.
OPCION_ANALIZAR_TERRENO = 1
OPCION_RECOLECTAR_MUESTRA = 2
OPCION_REALIZAR_OBSERVACION = 3
OPCION_FINALIZAR = 4

ENERGIA_ANALIZAR_TERRENO = 8
PROVISIONES_ANALIZAR_TERRENO = 0
PUNTOS_ANALIZAR_TERRENO = 10

ENERGIA_RECOLECTAR_MUESTRA = 12
PROVISIONES_RECOLECTAR_MUESTRA = 2
PUNTOS_RECOLECTAR_MUESTRA = 20

ENERGIA_REALIZAR_OBSERVACION = 5
PROVISIONES_REALIZAR_OBSERVACION = 0
PUNTOS_REALIZAR_OBSERVACION = 8

# --- Entrada de datos ---
energia_disponible = int(input("Energía disponible al llegar al destino: "))
provisiones_disponibles = int(input("Provisiones disponibles al llegar al destino: "))

# --- Valores iniciales del estado de la exploración ---
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
explorando = True

# --- Ciclo del menú ---
# El ciclo se repite mientras explorando sea True. Solo cambia a False
# cuando la tripulación elige finalizar o cuando una actividad no tiene
# recursos suficientes, así que el ciclo siempre termina por su condición.
while explorando:
    print()
    print("===== Menú de exploración =====")
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")
    opcion = int(input("Seleccione una opción: "))

    # --- Decisión múltiple: una rama por cada opción del menú ---
    if opcion == OPCION_ANALIZAR_TERRENO:
        # Decisión anidada: solo tiene sentido revisar los recursos
        # después de saber qué actividad se eligió.
        if (energia_disponible >= ENERGIA_ANALIZAR_TERRENO
                and provisiones_disponibles >= PROVISIONES_ANALIZAR_TERRENO):
            energia_disponible = energia_disponible - ENERGIA_ANALIZAR_TERRENO
            provisiones_disponibles = provisiones_disponibles - PROVISIONES_ANALIZAR_TERRENO
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + PUNTOS_ANALIZAR_TERRENO
            print("Actividad realizada: Analizar terreno. Puntos obtenidos:",
                  PUNTOS_ANALIZAR_TERRENO)
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            explorando = False
    elif opcion == OPCION_RECOLECTAR_MUESTRA:
        if (energia_disponible >= ENERGIA_RECOLECTAR_MUESTRA
                and provisiones_disponibles >= PROVISIONES_RECOLECTAR_MUESTRA):
            energia_disponible = energia_disponible - ENERGIA_RECOLECTAR_MUESTRA
            provisiones_disponibles = provisiones_disponibles - PROVISIONES_RECOLECTAR_MUESTRA
            actividades_realizadas = actividades_realizadas + 1
            muestras_recolectadas = muestras_recolectadas + 1
            puntos_cientificos = puntos_cientificos + PUNTOS_RECOLECTAR_MUESTRA
            print("Actividad realizada: Recolectar muestra. Puntos obtenidos:",
                  PUNTOS_RECOLECTAR_MUESTRA)
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            explorando = False
    elif opcion == OPCION_REALIZAR_OBSERVACION:
        if (energia_disponible >= ENERGIA_REALIZAR_OBSERVACION
                and provisiones_disponibles >= PROVISIONES_REALIZAR_OBSERVACION):
            energia_disponible = energia_disponible - ENERGIA_REALIZAR_OBSERVACION
            provisiones_disponibles = provisiones_disponibles - PROVISIONES_REALIZAR_OBSERVACION
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + PUNTOS_REALIZAR_OBSERVACION
            print("Actividad realizada: Realizar observación. Puntos obtenidos:",
                  PUNTOS_REALIZAR_OBSERVACION)
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            explorando = False
    elif opcion == OPCION_FINALIZAR:
        print("Exploración finalizada por la tripulación.")
        explorando = False
    else:
        # El estado no se modifica y el menú se vuelve a mostrar.
        print("Opción no válida.")

# --- Salida de resultados ---
print()
print("Actividades realizadas:", actividades_realizadas)
print("Muestras recolectadas:", muestras_recolectadas)
print("Puntos científicos:", puntos_cientificos)
print("Energía restante:", energia_disponible, "unidades")
print("Provisiones restantes:", provisiones_disponibles, "unidades")
