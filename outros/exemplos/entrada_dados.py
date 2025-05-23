# Entrada de dados 
nome = "Lucas"
idade = 25
print("Meu nome é " + nome + " e eu tenho " + str(idade) + " anos.")
print("Meu nome é {} e eu tenho {} anos. ".format(nome, idade))


# Estrutura de controle

numero = int(input("Insira o valor: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else: 
    print("O número é zero.")