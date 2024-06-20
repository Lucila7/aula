"""
Agora crie um script para uma lista de frutas, e outra lista com o nome alergias. Insira uma fruta da lista de frutas na lista de alergias. 

Depois crie um for para cada item da lista passar por uma verificação em uma estrutura condicional para verificar se essa fruta está contida na lista de alergias. Caso a fruta esteja na lista, imprima na tela o nome dela. 
"""

#criando as listas de frutas e de alergias

frutas = ['abacate', 'banana', 'caju', 'damasco', 'figo', 'goiaba', 'limao']

alergias = ['rinite', 'sinusite', 'urticaria', 'dermatite']

#adicionando uma fruta na lista de alergias
alergias.append('banana')
print(alergias)

print('-----------------')

#verificando se tem fruta na lista de alergias e imprimido-a

for fruta in frutas:
    if fruta in alergias:
        print(f'Você tem a fruta {fruta} na lista de alergias!')
    