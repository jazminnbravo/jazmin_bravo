def imprimir_tabla(ordenados):
    for nombre, data in ordenados:
        print(f"{nombre}: {data['total']} pts")

def imprimir_tabla_final(ordenados):
    print("Tabla de posiciones final:")
    print("Chef | Puntaje | Rondas Ganadas | Mejor Ronda | Promedio")
    print("-"*50)

    for nombre, data in ordenados:
        promedio = data["total"] / data["rounds"]
        print(f"{nombre} {data['total']} {data['wins']} {data['best']} {round(promedio)}")