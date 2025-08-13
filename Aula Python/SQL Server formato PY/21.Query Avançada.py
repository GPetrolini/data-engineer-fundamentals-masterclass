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

select 
t1.id as IdVenda
,t3.Nome as Produto
,t4.Categoria
,t1.total_price
,t2.status
,t2.created_at
,t5.first_name as NomeCliente
,t5.email
,t5.cell_phone as Telefone
,t5.state as Estado
from [dbo].[Items]									as T1	
Left Join  [dbo].[Ordens]						as T2 on t1.order_id = t2.id
Left join [dbo].[Produtos]					as T3 on t1.product_id= t3.ID
Left join [dbo].[Categoria]					as T4 on t3.Id_Category = t4.ID
Left join [dbo].[Clientes]				        as T5 on t2.customer_id = t5.id


"""

# %%
Join = pd.read_sql(Query,conexaoDB)
Join.head(10)


