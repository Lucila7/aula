#Atividade de receber o nome do usuário, altura e idade e imprimindo no terminal os dados.

nome = input("Digite o nome de usuário: ")
altura = float(input("Digite a sua altura em metros: "))
idade = int(input("Digite a sua idade: "))

print(" Seu nome de usuário é ", nome, ", sua altura é ", altura, "metros e a sua idade é ", idade, "anos.")

print(50*"-")

#Cálculo da média entre duas notas.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2

print("Sua primeira nota foi: ", nota1, ", a sua segunda nota foi: ", nota2, "e a sua média final é: ", media)