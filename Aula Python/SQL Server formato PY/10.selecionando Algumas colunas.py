# %%
import pandas as pd

# %%
df = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Clientes.csv", delimiter=',')
df.head()

# %%
# Selecionando colunas especificas
dfcolunas = df[["id","first_name","email","cell_phone"]]
dfcolunas.head(10)

# %% [markdown]
# #### Forma elegante

# %%
df = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Clientes.csv", delimiter=',')
df.head()

# %%
Colunas = ["id","first_name","email","cell_phone","state"] # variavel das colunas 
dfcolunas2= df[Colunas] # Df colunas especificas
dfcolunas2.head(10)


