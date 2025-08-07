# %%
import pandas as pd
df = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Clientes.csv", delimiter=',')
df

# %%
df['email'] = 1
df.head(10)

# %%
df['Nome Completo'] = df['first_name'] + ' ' + df['last_name']
df

# %%
df

# %%
print(df['created_at'].dtype)

# %%
# Converter a coluna 'created_at' para o formato de data
df['created_at'] = pd.to_datetime(df['created_at'])

# %%
print(df['created_at'].dtype)

# %%
df

# %%
# Adicionar coluna com o ano
df['ano'] = df['created_at'].dt.year
df

# %%
# Adicionar coluna com o mes
df['Mes'] = df['created_at'].dt.month
df

# %%
# Adicionar coluna com o dia
df['dia'] = df['created_at'].dt.day
df

# %%
# Adicionar coluna com o nome do mês em português
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
df['Nomemes'] = df['created_at'].dt.month.map(lambda x: meses[x-1])
df

# %%
# Adicionar coluna com o dia
df['Hora'] = df['created_at'].dt.hour
df['Minuto'] = df['created_at'].dt.minute
df['Segundo'] = df['created_at'].dt.second
df  

# %% [markdown]
# Juntar scriypt
# 

# %%
import pandas as pd
df = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Clientes.csv", delimiter=',')
df['created_at'] = pd.to_datetime(df['created_at']) # Convert para formato data 
df['ano'] = df['created_at'].dt.year                # Adicionar coluna ano
df['Mes'] = df['created_at'].dt.month               # Adicionar coluna com o dia
df['dia'] = df['created_at'].dt.day                 # Adicionar coluna com o dia
df['Hora'] = df['created_at'].dt.hour               # Adicionar hora
df['Minuto'] = df['created_at'].dt.minute           # Adicionar minuto
df['Segundo'] = df['created_at'].dt.second          # Adicionar segundo
# Adicionar coluna com o mês em português
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
df['Descmes'] = df['created_at'].dt.month.map(lambda x: meses[x-1])
df



# %%
#Filtro
Ano2018 = df.loc[df['ano'] == 2018]
Ano2018


# %%
Ano2018mes8 = df[(df['ano'] == 2018) & (df['Mes'] == 8)]
Ano2018mes8.head(30)



