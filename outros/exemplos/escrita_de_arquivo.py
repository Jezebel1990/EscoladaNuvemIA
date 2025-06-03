import csv
with open('dados.csv', 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['nome','idade','cidade'])
    escritor.writerow(['Paula','19','Mauá'])