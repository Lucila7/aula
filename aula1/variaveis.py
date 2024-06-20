"""
O aluno Matheus teve a primeira nota 2, a segunda nota 3, e a nota final 5

"""

nome = "Matheus"
n1 = 2
n2 = 3
soma = n1 + n2

print("O aluno ", nome , "teve a primeira nota " , n1 ,", a segunda nota ", n2,  ", e a nota final " ,soma)

nome2 = "PAULA"
sobrenome = "MARTINS"
mes = "JANEIRO"
valor = "500,00"
desconto = 10
cupom = "PAULAÉ10"

print("Olá,", nome2 , sobrenome ,". Em", mes, "você realizou uma compra no valor de R$", valor, "e ganhou um desconto de ", desconto, "% em sua próxima compra. Use o cupom ", cupom)

format_1 = f"O nome da pessoa é {nome}, desconto dela é {desconto}"
format_2 = "O nome da pessoa é {}, o desconto dela é {}". format(nome, desconto)
format_3 = "O nome da pessoa é {a}, o desconto dela é {b}". format(a=nome, b=desconto)

print(format_1)
print(format_2)
print(format_3)

tipo_nome = type(nome)
tipo_desconto = type(desconto)

print(tipo_nome)
print(tipo_desconto)