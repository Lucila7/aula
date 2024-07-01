"""O desafio é o seguinte: você vai criar uma lista de dados e, usando a biblioteca OS, interagir com o seu sistema operacional. Além disso, também criará uma nova pasta para salvar o arquivo de texto txt.
"""

import os

print(os.name)

#criando uma lista de dados
cidades = ['São Paulo', 'Rio de Janeiro', 'Porto Alegre', 'Vitória', 'Brasília']

#Criando uma pasta de dados
pasta = "dados"
os.makedirs(pasta, exist_ok=True)

arquivo = open(os.path.join(pasta, "cidades.txt"), "w")
arquivo.write("\n".join(cidades))
arquivo.close()

print('Tudo feito!')