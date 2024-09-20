'''
redondeo de numeros decimales
'''

def format_number(number):
    # Redondear el número a 2 decimales
    rounded_number = round(number, 2)
    # Formatear el número con exactamente 2 decimales
    return f"{rounded_number:.2f}"

# Ejemplo de uso
num1 = 5.5589
num2 = 3.3424

print(format_number(num1))  # Devuelve '5.56'
print(format_number(num2))  # Devuelve '3.34'
