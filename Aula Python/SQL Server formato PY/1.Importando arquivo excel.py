# %%
import pandas as pd

# %%
df = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Produto.xlsx")
df.head(5)

# %%
# df_calca = df.loc[df['coluna'] == 'Calça']  localizar 1 item especifico de uma coluna
df_calca = df.loc[df['Name'] == 'Vestido Super curto']

# %%
df_calca

# %%
itens = ['Calça','TV', 'Perfume','Fogão']
df_itens = df.loc[df['Name'].isin(itens)]


# %%
df_itens

# %%
df_itens2 = df.loc[df['Name'].isin(['Calça','TV', 'Sapato vermelho','Fogão'])]
df_itens2

# %%
#Localizar valor > que o que escolher
dfMais1000 = df.loc[df['Price'] > 1000] 

# %%
dfMais1000.head()

# %%
dfmenos1000 = df.loc[df['Price'] < 1000] 
dfmenos1000.head()


# %%
df200a1000 = df.loc[(df['Price'] > 200) & (df['Price'] <= 2000)]
df200a1000



