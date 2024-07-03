"""
Criar uma tabela.

"""
#importando a biblioteca para tabelas
import pandas as pd

#Inserindo os dados que irão para a tabela
data ={
    "Nome": ["João", "Marta", "Ary", "Matheus", "Michele"],
    "Idade": [51, 37, 23, 24, 33]
}

table = pd.DataFrame(data)

#imprimindo a tabela
print(table)