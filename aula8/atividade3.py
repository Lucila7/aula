import pandas as pd

dados = pd.read_csv('./dados_ficticios.csv')

df = pd.DataFrame(data=dados)

maiores_de_40 = df[df["idade"] > 40]
print(maiores_de_40)

renda_acima_5mil = df[df["renda"] > 5000]
print(renda_acima_5mil)

renda_acima_15mil = df[df["renda"] > 15000]
print(renda_acima_15mil)