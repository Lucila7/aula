import requests

response = requests.get('https://viacep.com.br/ws/01001000/json/')
data = response.json()
print(data)


cep = input("Qual o seu cep: ")

response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

data = response.json()

print(f'O logradouro desse cep é:', data['logradouro'])
print( data['logradouro'])