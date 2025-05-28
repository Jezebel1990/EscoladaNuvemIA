"""
Crie uma função que verifique se uma palavra ou frase é um
palíndromo (lê-se igual de trás para frente, ignorando
espaços e pontuação).

Se o resultado é True, responda “Sim”, se o resultado for
False, responda “Não”
"""

def is_palindromo(texto):
    # Remover os espaços e converter para minúsculas
    texto_limpo = ''.join(char.lower()
                         for char in texto
                         if char.isalnum())
    return texto_limpo == texto_limpo[::-1]


expressao = input("Insira uma expressão para verificação: ")
resultado = is_palindromo(expressao)

if resultado == True:
    resposta = "Sim"
else: 
    resposta = "Não"

print (f"A expressão { expressao} é um palindromo? {resposta}")