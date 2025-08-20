# %% [markdown]
# ### https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html

# %%
import pandas as pd

# %%
df = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Produto.xlsx")
df.head(10)


# %%
df.duplicated()

# %%
df.duplicated(['Name'])

# %%
Duplicados = df[df.duplicated()]

# %%
Duplicados

# %%
# Remova as duplicatas do DataFrame
df_sem_duplicatas = df.drop_duplicates()

# %%
df_sem_duplicatas

# %%
df = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Produto.xlsx")
df.head(10)

# %%
# Remova as duplicatas da coluna "ID"
df_sem_duplicatas2 = df.drop_duplicates(subset=['ID'])

# %%
df_sem_duplicatas2

# %%
df = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Produto.xlsx")
df.head(10)

# %%
# Remova diretamente  as duplicatas do DataFrame inplace
df.drop_duplicates(inplace=True)

# %%
df


