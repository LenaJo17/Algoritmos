'''
Cantidad de litros que se beben
'''

import math

def litres(time):
    # Calcular la cantidad de litros y redondear hacia abajo
    return math.floor(time * 0.5)

# Ejemplo de uso
time = 3  # Horas de ciclismo
result = litres(time)

print(f"Nathan beberá {result} litros de agua.")
