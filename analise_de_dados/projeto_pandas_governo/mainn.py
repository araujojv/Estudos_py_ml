import pandas as pd 

caminho_dados_viagem = "/home/joao/Estudos_py_ml/analise_de_dados/projeto_pandas_governo/2023_Viagem.csv"

df_viagens = pd.read_csv(caminho_dados_viagem, encoding="Windows-1252", sep=";")
print(df_viagens)