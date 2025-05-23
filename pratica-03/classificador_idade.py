"""
Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais).
"""
# Captura a idade do usuário
idade = int(input("Digite a sua idade: "))

# Verificação de idade 
if 0 <= idade <= 12:
    print("Você é criança.")
elif 13 <= idade <= 17:
    print("Você é adolescente.")
elif 18 <= idade <= 59:
    print("Você é adulto.")
else:
    print("Você é idoso.")
