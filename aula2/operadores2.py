# #Mini Case 3: Operações de teste

# Imagine que você está em um processo se seleção para ocupar uma vaga de QA e, para testarem seus conhecimentos sobre OPERADORES, propõem o seguinte:

# Desafio: Faça um código que permita, ao inserir um valor, o retorno de 5 outputs, sendo eles:
n1 = float(input("Digite um valor: "))

o1 = n1*2
o2 = n1*3
o3 = n1**2
o4 = n1**(1/2)
o5 = n1**(1/3)

print(f"O dobro de {n1} é {o1}.")
print(f"O triplo de {n1} é {o2}.")
print(f"O valor ao quadrado de {n1} é {o3}.")
print(f"A raiz quadrada de {n1} é {o4:.2f}.")
print(f"A raiz cúbica de {n1} é {o5:.2f}.")