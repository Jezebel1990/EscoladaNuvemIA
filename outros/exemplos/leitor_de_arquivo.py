import csv

with open('dados.csv', 'r', newline='') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)