"""
Crie um script com:

Uma função para criar personas, contendo nome, cidade, idade. 
Salve os dados dessas personas em um arquivo CSV.
Suba todos os arquivos para seu repositório.
"""


import pandas as pd
from faker import Faker

faker = Faker('pt_br')

def create_persona()->dict:
    data = {
    "nome" : faker.name(),
    "idade" : faker.random_int(min=18, max=110),
    "cidade" : faker.city()
    }
    return data
    
def generate_personas_qtd(number_of_personas:int)->list:
    # personas_list = []
    # for _in ranger(number_of_personas):
    # personas_list.append(create_persona())  
    # LIST COMPREHENSION
    # operadores ternários
    return [create_persona() for _ in range(number_of_personas)]  

lista_de_personas = generate_personas_qtd(3)

def create_df(data: dict)-> pd.DataFrame:
    df = pd.DataFrame(data)
    return df

df_lista_de_personas = create_df(lista_de_personas)

print(df_lista_de_personas)

def save_to_csv(filename:str, dataframe:pd.DataFrame)->None:
    dataframe.to_csv(filename, index=False)

df_lista_de_personas.to_csv('lista_de_personas.csv', index=False)

save_to_csv(filename='lista_de_personas.csv', dataframe=df_lista_de_personas)








