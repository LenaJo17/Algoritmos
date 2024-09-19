import math


def age_range(age):
    if age > 14:
        # Fórmula para mayores de 14 años
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)
    else:
        # Fórmula para 14 años o menos
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)

    return f"{min_age}-{max_age}"


# Ejemplo de uso
age1 = 27
age2 = 5
age3 = 17

print(age_range(age1))  # Devuelve '20-40'
print(age_range(age2))  # Devuelve '4-5'
print(age_range(age3))  # Devuelve '15-20'
