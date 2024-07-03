"""
Faça o código que dê boas vindas para nomes específicos.
"""
#definindo a função e recebendo o nome do usuário

def saudacao(nome):
    nome = str(input("Digite o seu nome: "))
    if nome == "João":
        print("Olá, " + nome + " seja bem vindo(a)")
    else:
        print("Olá, visitante, seja bem vindo")

#Chamada da função
saudacao("joao")