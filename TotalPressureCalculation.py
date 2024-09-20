'''
calculo de presion total
'''


def total_pressure(M1, M2, m1, m2, V, T):
    # Convertir la temperatura de Celsius a Kelvin
    T_kelvin = T + 273.15

    # Constante de gas en dm^3⋅atm⋅K^−1⋅mol^−1
    R = 0.082

    # Aplicar la fórmula para calcular la presión total
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_kelvin / V

    return P_total


# Ejemplo de uso
M1 = 44  # Masa molar del gas 1 (g/mol)
M2 = 28  # Masa molar del gas 2 (g/mol)
m1 = 30  # Masa presente del gas 1 (g)
m2 = 20  # Masa presente del gas 2 (g)
V = 10  # Volumen de la vasija (dm^3)
T = 25  # Temperatura en grados Celsius

# Calcular la presión total
P_total = total_pressure(M1, M2, m1, m2, V, T)

print(f"La presión total es: {P_total:.2f} atm")
