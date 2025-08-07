# %%

"""
pip install pandas
pip install --upgrade pandas
"""

'''
Tipo Inteiro (int)
Ponto Flutuante ou Decimal (float)
String (str)
String (Object)
Data (datetime)

'''

# %%
import pandas as pd

# %%
df = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Clientes.csv", delimiter=',')
df

# %% [markdown]
# ###                              Conversoes de dados

# %%
df['id'].dtype

# %%
print(df['id'].dtype)

# %%
print(df['created_at'].dtypes)
print(df['first_name'].dtypes)
print(df['id'].dtype)

# %%
df

# %%
for coluna in df.columns:
    print(f"Coluna: {coluna}, Tipo de dados: {df[coluna].dtypes}")


# %%
df

# %%
df['id'] = df['id'].astype(float)

# %%
print(df['id'].dtype)

# %%
df['number'] = df['number'].astype(str)

# %%
print(df['number'].dtype)

# %%
for coluna in df.columns:
    print(f"Coluna: {coluna}, Tipo de dados: {df[coluna].dtypes}")

# %% [markdown]
# ## Conversao Datas
# 

# %%
import pandas as pd

# %%
df = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Clientes.csv", delimiter=',')
df

# %%
print(df['created_at'].dtypes)

# %%
# Converter a coluna 'created_at' para o formato de data e hora
df['created_at'] = pd.to_datetime(df['created_at'])

# %%
print(df['created_at'].dtypes)

# %%
# Filtrar os dados para o intervalo de anos entre 2018 e 2020
df_filtrado = df[(df['created_at'].dt.year >= 2018) & (df['created_at'].dt.year <= 2020)]
df_filtrado


# %%
# Filtrar somente o ano de 2018 e o mês de janeiro
df_dt2 = df[(df['created_at'].dt.year == 2018) & (df['created_at'].dt.month == 1)]

# Imprimir o DataFrame filtrado
df_dt2.head(30)

# %% [markdown]
# Conversao formato brasileiro

# %%
df

# %%
# Converter a coluna 'created_at' para o formato de data no padrão brasileiro
df['created_at'] = df['created_at'].dt.strftime('%d/%m/%Y')



# %%
df

# %% [markdown]
# ## converter padrao BR no primeiro comando

# %%
import pandas as pd
df = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Clientes.csv", delimiter=',')
df['created_at'] = pd.to_datetime(df['created_at'])
df['created_at'] = df['created_at'].dt.strftime('%d/%m/%Y %H:%M:%S')
df



