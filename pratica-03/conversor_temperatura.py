"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

temperatura = float(input("Digite a temperatura : "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

# Verifica e realiza a conversão
if origem == destino:
    resultado = temperatura
elif origem == "C" and destino == "F":
    resultado = temperatura * 9 / 5 + 32
elif origem == "C" and destino == "K":
    resultado = temperatura + 273.15
elif origem == "F" and destino == "C":
    resultado = (temperatura - 32) * 5 / 9
elif origem == "F" and destino == "K":
    resultado = (temperatura - 32) * 5 / 9 + 273.15
elif origem == "K" and destino == "C":
    resultado = temperatura - 273.15
elif origem == "K" and destino == "F":
    resultado = (temperatura - 273.15) * 9 / 5 + 32
else:
    resultado = None

# Exibe o resultado
if resultado is not None:
    print(f"{temperatura:.2f}°{origem} equivale a {resultado:.2f}°{destino}")
else:
    print("Unidades inválidas. Use C, F ou K.")