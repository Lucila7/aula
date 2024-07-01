"""
Verificação do número de vogais existente em uma palavra fornecida pelo usuário.
"""
#recebendo a palavra digitada

palavra = str(input("Digite uma palavra: "))

#contando o número de vogais

vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

contagem = 0

for letra in palavra:
    if letra in vogais:
        vogais += 1
print(f"A palavra {palavra} tem {vogais} vogais.")
