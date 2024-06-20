nome_pet = input("Digite o nome do pet: ")

idade_pet = int(input("Digite a idade do seu cachorro: ")) 

idade_petHumano = idade_pet*7

print(idade_petHumano)

valor_banho_pequeno = 50.00
valor_banho_medio = 60.00
valor_banho_grande = 75.00

custo_banho_pequeno = 5
custo_banho_medio = 15
custo_banho_grande = 20

numero_banho = int(input("Quantidade de banhos: "))
periodo = 12
tamanho = input("Digite o tamanho do pet pequeno/medio/grande: ")

if(tamanho == "pequeno"):
    lucro = valor_banho_pequeno - custo_banho_pequeno

elif(tamanho == "medio"):
        lucro = valor_banho_medio - custo_banho_medio
    
else :
     lucro = valor_banho_grande - custo_banho_grande
        
lucro_final = lucro*numero_banho
print("Olá, ", nome_pet, "tem", idade_petHumano, "e nos últimos 12 meses o lucro com este animal foi de R$ ", lucro_final)