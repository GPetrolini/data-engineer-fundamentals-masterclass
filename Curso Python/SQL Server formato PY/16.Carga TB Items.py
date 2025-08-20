# %%
"""
Create table Items(
id				int,
order_id       int,
product_id   int,
quantity        int,
total_price         money
)

"""

# %%
import pandas as pd
import pyodbc 

server = 'DESKTOP-33OODCP' 
database = 'Python' 
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      f'SERVER={server};'
                      f'DATABASE={database};'
                      'Trusted_Connection=yes;')

cursor = conexaoDB.cursor()   # criando cursor de comando 

# %%
dados = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\items.xlsx")
str(dados.columns).replace("'","") 
dados.head(5)


# %%
cursor.execute('delete from [Items]')   #executa tarefa de  apagar dados
cursor.commit()

# %%
str(dados.columns).replace("'","")  # coluna de origem 

# %%
str(dados.columns).replace("'","")  # coluna de origem 


# %%
dados.head(5)

# %%

print(dados['total_price'].dtype)


# %%
dados['total_price'] = dados['total_price'].astype(float)

# %%
#inserção no banco de dados 
for index, linha in dados.iterrows():
    
    cursor.execute("Insert into [Items](id,order_id,product_id,quantity,total_price)values(?,?,?,?,?)",linha.id,linha.order_id,linha.product_id,linha.quantity,linha.total_price) 
     # inserir colunas e quantas colunas tiver passar quantidade de ??
cursor.commit()   # validar dados no SQL Server
cursor.close()    #Fechar Cursor
conexaoDB.close() #Fechar Conexao

# %% [markdown]
# 


