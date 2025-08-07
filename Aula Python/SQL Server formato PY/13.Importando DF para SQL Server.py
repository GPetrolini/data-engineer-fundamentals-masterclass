# %% [markdown]
# # Bibliotecas

# %%
"""
create table Produtos(
    ID INT,
    Nome NVARCHAR(255),
    Price money,
    Id_Category INT
)
"""

# %%
#!pip install pyodbc 

import pandas as pd
import pyodbc 

server = 'DESKTOP-33OODCP' 
database = 'Python' 
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      f'SERVER={server};'
                      f'DATABASE={database};'
                      'Trusted_Connection=yes;')

cursor = conexaoDB.cursor()   # criando cursor de comando 

# %% [markdown]
# #### Conexão com senha

# %%
"""
server = 'DESKTOP-33OODCP'
database = 'Produtos'
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      f'SERVER={server};'
                      f'DATABASE={database};'
                      f'usuario= *********;'
                      f'senha=********;'                      
                      'Trusted_Connection=yes;')

cursor = conexaoDB.cursor()   # criando cursor de comando
"""

# %%
dados = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Produto.xlsx")
#display(dados)
dados.head(5)
#display(dados)

# %%
dados.columns

# %%
str(dados.columns).replace("'","") 


# %%
#Conversão de dados
#df['Nome'] = df.Nome.astype(str)  ##conversao de dados para string nvarchar 

# %% [markdown]
# # Inserindo DataFrame no Banco

# %%
dados.head(5)

# %%
for index, linha in dados.iterrows():
    
    cursor.execute("Insert into [Produtos](ID,Nome,Price,Id_Category)values(?,?,?,?)",linha.ID,linha.Nome,linha.Price,linha.Id_Category) 
     # inserir colunas e quantas colunas tiver passar quantidade de ??
cursor.commit()   # validar dados no SQL Server
cursor.close()    #Fechar Cursor
conexaoDB.close() #Fechar Conexao

# %% [markdown]
# 

# %%
#cursor.execute('delete  from [dbo].[Dim_Produto]')   #executa tarefa de  apagar dados
#cursor.commit()


