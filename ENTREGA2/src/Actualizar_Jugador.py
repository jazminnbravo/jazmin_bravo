def actualizar_(stats, player, total):
    stats[player]["total"] += total
    stats[player]["rounds"] += 1

    if total > stats[player]["best"]:
        stats[player]["best"] = total

#puntos,ronda,mejor puntaje 