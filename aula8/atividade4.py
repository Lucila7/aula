"""
Crie uma persona com a biblioteca Faker com nome, idade e cidade. Criando o atributo random.int para gerar valores aleatórios para idade.
"""

from faker import Faker

faker = Faker('pt_br')

persona = {
    'nome': faker.name(),
    'idade': faker.random_int(min=1, max=110),
    'cidade': faker.city()
}

print(persona)