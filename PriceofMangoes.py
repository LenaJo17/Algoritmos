def mango_cost(quantity, price_per_mango):
    # Calcular el número de mangos que se pagan (2 por cada 3)
    paid_mangoes = (quantity // 3) * 2 + (quantity % 3)

    # Calcular el costo total
    total_cost = paid_mangoes * price_per_mango

    return total_cost


# Ejemplo de uso
quantity = 9  # Cantidad de mangos
price_per_mango = 5  # Precio por mango

result = mango_cost(quantity, price_per_mango)
print(f"El costo total de los mangos es: {result} unidades monetarias.")
