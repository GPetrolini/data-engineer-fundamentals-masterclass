# %%
"""
Create table Ordens(
id				int,
created_at       datetime,
customer_id   int,
status        nvarchar(255)
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
dados = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Ordens.xlsx")
#str(dados.columns).replace("'","") 
#dados.head(5)


# %%
cursor.execute('truncate table  [Ordens]')   #executa tarefa de  apagar dados
cursor.commit()

# %%
str(dados.columns).replace("'","")  # coluna de origem 

# %%

#print(dados['total_price'].dtype)
#dados['total_price'] = dados['total_price'].astype(float)

# %%
#inserção no banco de dados 
for index, linha in dados.iterrows():
    
    cursor.execute("Insert into [Ordens](id,created_at,customer_id,status)values(?,?,?,?)",linha.id,linha.created_at,linha.customer_id,linha.status) 
     # inserir colunas e quantas colunas tiver passar quantidade de ??
cursor.commit()   # validar dados no SQL Server
cursor.close()    #Fechar Cursor
conexaoDB.close() #Fechar Conexao

# %% [markdown]
# 


