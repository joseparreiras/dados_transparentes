import pandas as pd
import os

os.chdir("D:\Scrapy Projects\dados_transparentes")

obitos = pd.read_json('obitos.json')
casos = pd.read_json('casos.json')

obitos_df = {obitos.Nome[i]:{obitos.Data[i][j]:obitos.Óbitos[i][j] for j in range(len(obitos.Data[i]))} for i in range(len(obitos))}
casos_df = {casos.Nome[i]:{casos.Data[i][j]:casos.Casos[i][j] for j in range(len(casos.Data[i]))} for i in range(len(casos))}

pd.DataFrame(obitos_df).to_csv('obitos.csv')
pd.DataFrame(casos_df).to_csv('casos.csv')
