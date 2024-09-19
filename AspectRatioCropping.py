import math

def to_16_9_aspect_ratio(x, y):
    # Calcular el nuevo ancho basado en la relación 16:9 manteniendo la altura (y)
    new_x = math.ceil(y * 16 / 9)
    return new_x, y

# Ejemplo de uso
x = 1440
y = 1080
new_resolution = to_16_9_aspect_ratio(x, y)

print(f"Resolución original: {x}x{y}")
print(f"Resolución ajustada a 16:9: {new_resolution[0]}x{new_resolution[1]}")
