"""Crie um programa que permita a um professor registrar as
notas de uma turma. O programa deve continuar solicitando
notas até que o professor digite 'fim'. Notas válidas são de 0 a
10. O programa deve ignorar notas inválidas e continuar
solicitando. No final, deve exibir a média da turma.
"""

notas = []

while True:
    try:
        entrada = input("Digite uma nota (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break

        numero = float(entrada)

        if 0 <= numero <= 10:
            notas.append(numero)
        else:
            print("Nota fora do intervalo válido (0 a 10).")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim' para encerrar.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")
