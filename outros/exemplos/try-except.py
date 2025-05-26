try:
    numero = int(input("Digite um número: "))
except ValueError:
    print ("Valor inválido! Por favor, insera um número.")
print(f"O valor é: {numero}")