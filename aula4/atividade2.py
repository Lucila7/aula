"""
Crie a estrutura de uma tabuada para um valor inserido. O resultado deverá ser printado do valor multiplicado de 1 a 10. 
"""
#obtendo o valor a ser utilizado na multiplicação
valor_inserido = int(input("Digite um valor: "))

#imprimindo a valor inserido e calculando a multiplicação do valor de 1 até 10
for i in range(1,11):
    print(f"{valor_inserido} x {i} = {valor_inserido *i}")
