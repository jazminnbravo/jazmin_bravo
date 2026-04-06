def obtener_ganador(scores_round):
    return max(scores_round, key=scores_round.get) #mas puntos tiene 


def ordenar_tabla(stats):
    return sorted(stats.items(), key=lambda x: x[1]["total"], reverse=True) #ordena el ranking 