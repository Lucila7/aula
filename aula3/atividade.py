#Construa um script para verificar se o usuário tem uma idade maior que 18 anos, se tiver, imprima na tela #"Indivíduo possui idade mínima para dirigir
idade = int(input("Digite a sua idade: "))
if idade > 18 :
    print("Indivíduo possui idade mínima para dirigir")

    #USANDO ELIF: #Complemente o script feito, imprimindo na tela #"Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir"
elif 17<idade<=18:
    print("Ainda NÃO está apto para dirigir ")

#USANDO ELSE: #Complemente o script feito, imprimindo na tela #"Indivíduo NÃO possui idade mínima para dirigir"

else:
    print("indivíduo NÃO possui idade mínima para dirigir")