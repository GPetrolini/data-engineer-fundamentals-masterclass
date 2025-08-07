# %%
import pandas as pd

# %%
df = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Clientes.csv",delimiter=',')
df.head(5)

# %%
# Filtrar 1 item especifico de uma coluna
estado = df.loc[df['state'] == 'Santa Catarina']

# %%
estado

# %%
df

# %%
# Escolher estados específicos
estados = ['Rio de Janeiro','São Paulo',]
Df_estados = df.loc[df['state'].isin(estados)]
Df_estados

# %%
df_estados2 = df.loc[df['state'].isin(['Rio de Janeiro','Santa Catarina','Sergipe'])]
df_estados2

# %%
Df_estados2 = df.loc[df['state'].isin(['Rio de Janeiro','Ceará', 'Rondônia','Bahia','Ceará', 'Rondônia','Bahia','Ceará',    
                                       'Rondônia','Bahia','Ceará', 'Rondônia','Bahia','Ceará', 'Rondônia','Bahia','Ceará',  
                                       'Rondônia','Bahia','Ceará', 'Rondônia','Bahia','Ceará', 'Rondônia','Bahia','Ceará',  
                                       'Rondônia','Bahia'])]
Df_estados2

# %% [markdown]
# # Tratando Nulos
# 

# %%
import pandas as pd

# %%
df = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Clientes.csv",delimiter=',')
df.head(5)

# %%
# Substituir valores nulos
df['street'] = df ['street'].fillna('Não registrado')
df

# %%
#Substituir valores nulos
df['street'] =           df['street'].fillna('Nao Cadasatrado')
df['email'] =            df['email'].fillna('Email Não Cadastrado')
df['number'] =           df['number'].fillna('Sem Numero')
df['additionals'] =      df['additionals'].fillna('Sem Info')


# %% [markdown]
# #### Metodo Replace

# %%
# Substituindo os nomes dos estados no DataFrame
"""
df['Coluna'] = df['coluna'].replace(valor_original, valor_substituto)
"""

# %%
# resetar DF
df = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Clientes.csv",delimiter=',')
df.head(5)

# %%
df['state'] = df['state'].replace('São Paulo', 'SP')
df['state'] = df['state'].replace('Acre', 'AC')
df['state'] = df['state'].replace('Distrito Federal', 'DF')


# %%
df.head(20)

# %%
# resetar DF
df = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Clientes.csv",delimiter=',')
df.head(5)

# %%
# Fazendo a substituição de um valor específico
valor_original = 'São Paulo'
valor_substituto = 'SP'
df['state'] = df['state'].replace(valor_original, valor_substituto)


# %%
df.head(30)

# %%
import pandas as pd
# Resetar DF
df = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Clientes.csv",delimiter=',')
df.head()

# %%
# Mapeando os nomes dos estados para substituição
# Obs itens criados entre chves {} significa dicionario
mapeamento = {'Maranhão': 'Maranhao', 'Piauí': 'Piaui', 'Goiás': 'Goias','São Paulo':'SPteste'}

# Substituindo os nomes dos estados no DataFrame
df['state'] = df['state'].replace(mapeamento)


# %%
df.head(30)


