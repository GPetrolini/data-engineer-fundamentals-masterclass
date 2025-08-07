# %%
import pandas as pd
import os

# %%

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
#consolidado



# %% [markdown]
# ##### Verificar se arquivo ja existe e excluir 
# 

# %%
# Caminho da pasta onde será salvo o arquivo Excel
pasta_destino = r'C:\\Users\\Admin\\Documents\\data-engineer-fundamentals-masterclass\\data-engineer-fundamentals-masterclass\\Origem de dados\\arquivos_csv\\Consolidar\\Arquivos consolidados'

# Nome do arquivo Excel (variável)
nome_arquivo = 'VendasGeraldelete.xlsx'

# Caminho completo do arquivo Excel
Caminho_Completo = pasta_destino + nome_arquivo 

# Verificar se o arquivo Excel já existe
if os.path.exists(Caminho_Completo):
    # Excluir o arquivo existente
    os.remove(Caminho_Completo)
    #print(f"Arquivo {nome_arquivo} existente foi excluído.")


# Salvar o DataFrame como arquivo Excel
consolidado.to_excel(Caminho_Completo, index=False)



