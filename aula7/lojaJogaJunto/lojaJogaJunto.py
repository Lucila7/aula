"""
A Loja do Joga Junto conta mais uma vez com a colaboração do seu squad! Desta vez, surge a necessidade de desenvolver um programa que analisa o CEP inserido pelo usuário e determina se ele é elegível para frete grátis. Para realizar essa tarefa, foi definida uma política de frete grátis abrangendo todos os estados das regiões Norte e Nordeste do país.  

Faça um brainstorming com sua equipe sobre o fluxo e requisitos necessários para construção desse programa

Desenvolva o programa

Faça casos de teste para este cenário, documente os testes realizados e insira no Bitrix

Caso seja encontrado algum bug no seu código, documente-o. 
"""

import requests

#definindo estados do norte
def verificar_norte(estado):
    estados_norte = ["AC", "AM", "AP", "PA", "RR", "RO", "TO"]
    return estado in estados_norte

#definindo os estados do nordeste
def verificar_nordeste(estado):
    estados_nordeste = ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]
    return estado in estados_nordeste

#Verificando se o cep tem direito à frete grátis
def frete_gratis(estado):
    if verificar_norte(estado) or verificar_nordeste(estado):
        return "Você tem direito à Frete Grátis"
    else:
        return "O CEP informado não tem direito à Frete Grátis."
  
cep = int(input("Qual o seu cep: "))

response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
data = response.json()

print(data)
estado = data['uf']

entrega = frete_gratis(estado)

print(f'O uf desse cep é:', data['uf'])
print(entrega)