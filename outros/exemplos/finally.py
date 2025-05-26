try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")
finally:
    arquivo.close()
    print("Arquivo fechado")