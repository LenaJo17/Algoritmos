def usd_to_cny(usd):
    # Tasa de conversión de USD a CNY
    conversion_rate = 6.75

    # Convertir USD a CNY
    cny = usd * conversion_rate

    # Formatear el resultado como cadena con dos decimales
    return f"{cny:.2f} Chinese Yuan"


# Ejemplo de uso
usd_amount = 100
result = usd_to_cny(usd_amount)

print(result)  # Devuelve '675.00 Chinese Yuan'
