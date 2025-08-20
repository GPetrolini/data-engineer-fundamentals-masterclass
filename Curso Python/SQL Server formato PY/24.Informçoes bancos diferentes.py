# %%
import pandas as pd
import pyodbc 

server = 'DESKTOP-33OODCP' 
database = 'Python' 
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      f'SERVER={server};'
                      f'DATABASE={database};'
                      'Trusted_Connection=yes;')

cursor = conexaoDB.cursor()

# %%
Query = """
select * from [dbo].[Items]
where total_price >5000

"""

# %%
Vendas = pd.read_sql(Query,conexaoDB)
Vendas.head(10)

# %% [markdown]
# Criar conexão com 2° banco de dados / servidor
# 

# %%
server2 = 'DESKTOP-33OODC'
database2= 'Produtos' 
conexaoDB2 = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      f'SERVER={server2};'
                      f'DATABASE={database2};'
                      'Trusted_Connection=yes;')

cursor2 = conexaoDB2.cursor()   # criando cursor de comando 

# %%
Query2="""

SELECT *
FROM [Produtos].[dbo].[Dim_Produto]

"""

# %%
Produtos= pd.read_sql(Query2,conexaoDB2)


# %%
Vendas.head(5)

# %%
Produtos.head(5)

# %%
Vendas ["product_id"] = Vendas ["product_id"].astype(int)
Produtos ["Id"] = Produtos ["Id"].astype(int)

# %%
join = pd.merge(Vendas,Produtos,left_on="product_id",right_on="Id",how="left")

# %%
join.head(10)

# %%
cursor.close
conexaoDB.close
cursor2.close
conexaoDB2.close


