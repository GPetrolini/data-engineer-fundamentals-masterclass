# %% [markdown]
# Importacao DFS

# %%
import pandas as pd

# %%
Produto = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Produto.xlsx")
Categoria = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Categoria.xlsx")
Itens = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\items.xlsx")
Ordens = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Ordens.xlsx")
Clientes = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Clientes.csv",delimiter=',')


# %%
Ordens.head(5)

# %%
Clientes.head(5)

# %%
T1=pd.merge(Ordens,Clientes , left_on="customer_id" ,right_on="id", how="left")

#left_on        chave da tabela a esquerda
#right_on       chave da tabela a Direita
#how            Tipo de Join 

#Tipos de Join 
#left  todos dados da tabela a esqueda(1° tabela) e completa com restante que achar
#right todos dados da tabela a Direita(2° tabela) e completa com restante que achar
#inner retorna dados apenas quando as duas tabelas tem chaves
#outer  este retorna todos os registros de ambas as tabelas.


# %%
T1.head(5)

# %%
T1 = T1[["id_x","created_at_y","first_name","cell_phone","state"]]
T1.head(10)

# %% [markdown]
# ![image.png](attachment:image.png)

# %%
Itens.head(5)

# %%
Produto.head(5)

# %%
T2=pd.merge(Itens,Produto ,left_on="product_id" , right_on="ID" ,how="left")
T2= T2[["id","Nome","Id_Category"]]
T2.head(5)


# %%
Categoria.head(5)

# %%
CatProd= pd.merge(T2,Categoria ,left_on= "Id_Category" ,right_on="id" , how="left")
CatProd.head(15)


