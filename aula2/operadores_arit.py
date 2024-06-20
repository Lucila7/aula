# Fazer um programa que some 4 notas e, no final, tenha a média aritmética dessas notas.

nome = input("Digite o seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print("Olá, ", nome, "! Sua média é: ", media, "pontos.")
print(f"Olá, {nome}! Sua média é:{media:.2f} pontos.")