"""
Projeto final do módulo Python em que é feito a criação de um usuário, seu devido login no endpoint referido e é salvo o json de resposta do login.
"""

#importando as bibliotecas necessárias para o projeto
import requests
from faker import Faker
import json

#criação de dados em português-brasileiro
faker = Faker('pt_br')

#criação de um dicionário de dados em inglês, de acordo com o endpoint
def user():
    request_data = {
        "username": faker.user_name(),
        "email": "mail4@ijj.com",  
        "phone": faker.phone_number() ,
        "address": faker.address(),
        "cpf": faker.cpf(),
        "password": "987654321"
    }
    return request_data
print(user())

#fazendo o post do novo usuário
response = requests.post(url ='https://desafiopython.jogajuntoinstituto.org/api/users/', data = user())

response_data = response.json()
#imprimindo os dados do post
print(response_data)

#Inserindo os dados necessário para o login do usuário
def login():
    request_login = {
        "email": "mail4@ijj.com",
        "password": "987654321"
    }
    return request_login

#executando o login do usuário criado
login = requests.post(url = 'https://desafiopython.jogajuntoinstituto.org/api/users/login/', data = login())
logado = login.json()
print(logado)

#salvando a resposta do login em um arquivo json
with open('logados2.json', 'w') as outfile:
        json.dump(logado, outfile)

print("Resposta de login salvo em logados2.json")





