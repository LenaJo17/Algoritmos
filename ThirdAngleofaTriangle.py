def find_third_angle(angle1, angle2):
    # La suma de los ángulos de un triángulo siempre es 180 grados
    return 180 - (angle1 + angle2)

# Ejemplo de uso
angle1 = 60
angle2 = 60
third_angle = find_third_angle(angle1, angle2)

print(f"El tercer ángulo es: {third_angle} grados")
