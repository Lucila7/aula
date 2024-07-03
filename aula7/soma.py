"""
Faça um código para formar a soma de dois números, usando o comando 'return'.
"""

#Recebendo dois números aleatórios
def soma(n1, n2):
    conta = n1 + n2
    return conta

valor1 = float(input("Digite um número: "))
valor2 = float(input("Digite outro número: "))

calculo = soma(valor1, valor2)
print(f"A soma dos números {valor1} e {valor2} é {calculo} ")