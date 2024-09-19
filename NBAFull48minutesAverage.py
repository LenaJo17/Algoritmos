def points_per_48(ppg, mpg):
    # Si mpg es 0, retornamos 0
    if mpg == 0:
        return 0

    # Extrapolar los puntos a 48 minutos y redondear a la décima más cercana
    ppg_48 = (ppg / mpg) * 48
    return round(ppg_48, 1)


# Ejemplo de uso
ppg = 25  # Puntos por juego
mpg = 30  # Minutos por juego

result = points_per_48(ppg, mpg)
print(f"Puntos extrapolados a 48 minutos: {result}")
