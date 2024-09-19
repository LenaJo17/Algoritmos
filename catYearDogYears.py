def calculate_pet_ages(human_years):
    # Calcular años de gato
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Calcular años de perro
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

        # Devolver los resultados en un diccionario
        return {
            "humanYears": human_years,
            "catYears": cat_years,
            "dogYears": dog_years
        }

# Ejemplo de uso
human_years = 10
result = calculate_pet_ages(human_years)

print(result)  # Devuelve [humanYears, catYears, dogYears]
print(type(result))