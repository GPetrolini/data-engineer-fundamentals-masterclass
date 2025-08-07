# %%
import pandas as pd
import os

# Diretório dos arquivos Excel
diretorio = (r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Consolidar")
# Lista para armazenar os dados dos arquivos
dados = []

# Iterar sobre os arquivos Excel no diretório
for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.xlsx'):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        df = pd.read_excel(caminho_arquivo)
        dados.append(df)

# Consolidar os dados em um único DataFrame
consolidado = pd.concat(dados)
consolidado



