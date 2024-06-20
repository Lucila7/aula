#Crie um script com as seguintes instruções, pesquisando na internet como fazer:

#Crie uma tupla com 5 dados
cores = ("amarelo", "vermelho", "azul", "verde", "branco")

print("As cores da tupla são: ",cores)
print(50*"_")

#Altere a tupla para uma lista

cores = ["amarelo", "vermelho", "azul", "verde", "branco"]

print("As cores da lista são: ",cores)
print(50*"_")

#Insira 2 dados extras a essa lista
cores = ["amarelo", "vermelho", "azul", "verde", "branco"]

cores.extend(["roxo", "rosa"])
print("As cores da lista nova são: ",cores)
print(50*"_")

#Remova o primeiro dado da lista
cor_removida = cores.pop(0)
print("A cor removida foi: ",cor_removida)
print("As cores da lista são: ",cores)
print(50*"_")

#Remova o último dado da lista
ultima_removida = cores.pop()
print("A cor removida foi: ",ultima_removida)
print("As cores da lista são: ",cores)
print(50*"_")

#Faça um print com o primeiro dado da lista
print("A primeira cor da lista é: ",cores[0])
print(50*"_")

#Faça um print com a quantidade de dados da lista
quantidade = len(cores)
print("A quantidade de itens na lista de cores é: ", quantidade)
print(50*"_")

#Crie um dicionário com os seguintes dados:
#Nome, Idade, Profissão
dados_pessoas = []

numero_pessoas = int(input("Quantas pessoas você quer adicionar? "))

for i in range(1, numero_pessoas + 1):
    pessoa = {}
    pessoa["nome"] = input(f"Digite o nome da pessoa {i}: ")
    pessoa["idade"] = int(input(f"Digite a idade da pessoa {i}: "))
    pessoa["profissão"] = input(f"Digite a profissão da pessoa {i}: ")

    # Adicionando o dicionário da pessoa na lista
    dados_pessoas.append(pessoa)

    # Convertendo a lista de dicionários em um único dicionário com nomes como chaves
dicio_pessoas = {"nome": pessoa["nome"], "idade": pessoa["idade"], "profissao": pessoa["profissão"]}

print(50*"_")
print(dicio_pessoas)
print(50*"_")

nomes = [pessoa["nome"] for pessoa in dados_pessoas]
print("\n Nomes das pessoas no dicionário: ", nomes)
print(50*"_")