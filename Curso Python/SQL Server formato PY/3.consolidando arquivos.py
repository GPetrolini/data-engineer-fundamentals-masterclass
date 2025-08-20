# %%
import pandas as pd
import os

# %%
vendas2021 = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Consolidar\Vendas2021.xlsx")
vendas2022 = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Consolidar\Vendas2022.xlsx")
vendas2023 = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Consolidar\Vendas2023.xlsx")

# %%
vendas2021.head(3)

# %%
vendas2022.head(3)

# %%
vendas2023.head(3)

# %% [markdown]
# ### Consolidando arquivos de uma pasta

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



# %% [markdown]
# ##### Salvando consolidado em uma pasta especifica Formato Excel

# %%
# Caminho da pasta onde será salvo o arquivo Excel
pasta_destino = r'C:\\Users\\Admin\\Documents\\data-engineer-fundamentals-masterclass\\data-engineer-fundamentals-masterclass\\Origem de dados\\arquivos_csv\\Consolidar\\Arquivos consolidados'

# Nome do arquivo Excel (variável)
nome_arquivo = 'VendasGeral.xlsx'

# Caminho completo do arquivo Excel
Caminho_Completo = pasta_destino + nome_arquivo 

# Salvar o DataFrame como arquivo Excel
consolidado.to_excel(Caminho_Completo, index=False)


# %% [markdown]
# ##### Salvando consolidado em uma pasta especifica Formato CSV

# %%
# Caminho da pasta onde será salvo o arquivo CSV
pasta_destino = r'C:\\Users\\Admin\\Documents\\data-engineer-fundamentals-masterclass\\data-engineer-fundamentals-masterclass\\Origem de dados\\arquivos_csv\\Consolidar\\Arquivos consolidados'

# Nome do arquivo Excel (variável)
nome_arquivo = 'VendasGeral.csv'

# Caminho completo do arquivo Excel
Caminho_Completo = pasta_destino + nome_arquivo

# Salvar o DataFrame como arquivo CSV
consolidado.to_csv(Caminho_Completo, index=False,sep=',')


# %% [markdown]
# ##### Salvando consolidado em uma pasta especifica Formato TXT

# %%

# Caminho da pasta onde será salvo o arquivo Excel
pasta_destino = r'C:\\Users\\Admin\\Documents\\data-engineer-fundamentals-masterclass\\data-engineer-fundamentals-masterclass\\Origem de dados\\arquivos_csv\\Consolidar\\Arquivos consolidados'

# Nome do arquivo Excel (variável)
nome_arquivo = 'VendasGeral.txt'

# Caminho completo do arquivo Excel
Caminho_Completo = pasta_destino + nome_arquivo

# Salvar o DataFrame como arquivo Excel
consolidado.to_csv(Caminho_Completo, index=False,sep=',')

# %% [markdown]
# ###                             Resmumo treino

# %%
# bibliotecas
import pandas as pd
import os

# Diretório dos arquivos CSV
diretorio = (r"K:\Python\Arquivos\Origem\arquivos_excel\Consolidar")

# Lista para armazenar os dados dos arquivos
dados = []

# Iterar sobre os arquivos Excel no diretório
for arquivo in os.listdir(diretorio):                        # loop na pasta (diretório)
    if arquivo.endswith('.xlsx'):                            # achar somente arquivos excel
        caminho_arquivo = os.path.join(diretorio, arquivo)   # pecorrer cada arquivo 
        df = pd.read_excel(caminho_arquivo)                  # ler os dados 
        dados.append(df)                                     # armazenar na ultima linh 1 a 1 dos arquivos

# Consolidar os dados em um único DataFrame
consolidado = pd.concat(dados)
consolidado.head()



