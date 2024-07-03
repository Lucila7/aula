"""
Crie um DataFrame com os seguintes dados:

Nome, idade e cidade. Sendo 3 pessoas moradoras de Recife, 2 de Salvador, 1 de são paulo e 1 de Manaus

Depois, filtre os dados para exibir na tela apenas os moradores do Recife. 
"""

#importando a biblioteca para tabelas
import pandas as pd

#Inserindo os dados que irão para a tabela
data = {
    "Nome": ["Marcos", "Maria", "Ana", "Caio", "Mia", "Théo", "José"],
    "Idade": [43, 25, 31, 69, 20, 37, 65],
    "Cidade": ["Recife", "Salvador", "São Paulo", "Recife", "Manaus", "Recife", "Salvador"]
}

df = pd.DataFrame(data)
print(df)

recife = df[df["Cidade"] == "Recife"]

#imprimindo a tabela

print(recife)