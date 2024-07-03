def calcular_preco_total(valor_total, desconto_percentual):
    desconto = valor_total * (desconto_percentual / 100)
    preco_com_desconto = valor_total - desconto
    return preco_com_desconto

valor_da_compra = float(input( "Digite o valor da compra:"))
desconto_oferecido = int(input("Porcentagem de desconto:"))

preco_final = calcular_preco_total(valor_da_compra, desconto_oferecido)
print("O valor final da compra é: R$  ", preco_final)
