"""Faça um for e imprima na tela todos os numeros de 1 até 1000. Depois, crie uma estrutura condicional para descobrir e printar apenas os números que forem par. 
 """

#imprimindo números de 1 a 1000
for i in range(1,1001):
    print(i)

print(20*"-")

#imprimindo número pares
for i in range(1,1001):
    if i % 2 == 0:
        print(i)