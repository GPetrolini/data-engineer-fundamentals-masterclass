# %%
import pandas as pd

# %%
dados = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Produto.xlsx")
dados.head(10)


# %%
#ordem crescente coluna especifica
dados   =    dados.sort_values(by=['Name'])
dados.head(7)

# %%
#ordem crescente coluna especifica
dados=dados.sort_values(by=['Name'],ascending = False )
dados

# %%
#ordem crescente coluna especifica
dados=dados.sort_values(by=['Name'],ascending= False)
dados

# %% [markdown]
# #### Renomeando Colunas

# %%
dados = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Produto.xlsx")
dados.head(10)

# %%
# Renomeie as colunas do DataFrame
dados = dados.rename(columns={'Name':'Nome','Price':'Preco','Id_Category':'IdCategoria'})
#[]  lista
#{}   Dicionario

# %%
dados.head(10)

# %% [markdown]
# #### modo com variavel

# %%
dados = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Produto.xlsx")
dados.head(10)

# %%
# Crie um dicionário com os nomes das colunas antigos e novos
novascolunas = {'Name': 'Nome','Price': 'Valor'}
dados = dados.rename(columns = novascolunas)


# %%
dados.head(5)

# %% [markdown]
# Dados resumido 

# %%
import pandas as pd  # bibliotecas

# %%
dados = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Produto.xlsx")
novascolunas = {'Name': 'Nome','Price': 'Valor','Id_Category':'IdCategoria'}
dados = dados.rename(columns = novascolunas)
dados.head(10)


