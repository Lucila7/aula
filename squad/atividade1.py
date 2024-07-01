import requests
"""
Faça um ambiente virtual, instale o request e faça o código com os seguintes requisitos:
-Tenha uma estrutura de dicionário com nome e cep de cada integrante. Essa estrutura deverá ser salva em uma variável apenas.
-Faça uma requisição e imprima o nome e a cidade de cada integrante do squad. 
-Gere um arquivo chamado requirements.txt que contenha todas as dependências do seu projeto.
-Ao final, suba a atividade em seu github.
"""
#Crianco dicionário com nome e cep dos integrantes da squad

squad = {"Daniel": "11089050",
         "Lucila": "12410010",
         "Murillo": "11629224"}

#Requisição para cada integrante da squad
for integrante in squad:
    response = requests.get(f'https://viacep.com.br/ws/{squad[integrante]}/json/')
    data = response.json()
    print(f"{integrante} reside em {data['localidade']}")

    



