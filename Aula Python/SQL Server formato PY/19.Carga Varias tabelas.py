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

# %% [markdown]
# Importacao DFS

# %%
Produto = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Produto.xlsx")
Categoria = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Categoria.xlsx")
Itens = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\items.xlsx")
Ordens = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Ordens.xlsx")
Clientes = pd.read_csv(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_csv\Clientes.csv",delimiter=',')


# %%
Produto.head(10)

# %%
Categoria.head(10)

# %%
Itens.head(10)

# %%
Ordens.head(10)

# %%
Clientes.head(10)

# %% [markdown]
# deleta dados das tabelas

# %%
cursor.execute(
"""
truncate table [dbo].[Categoria]
truncate table [dbo].[Clientes]
truncate table [dbo].[Items]
truncate table [dbo].[Ordens]
truncate table [dbo].[Produtos]

"""
)   #executa tarefa de  apagar dados
cursor.commit() #validar os dados no sql server para bloquear usuario

# %% [markdown]
# Insere dados Passo a Passo 

# %%
#Carga Produto
for index, linha in Produto.iterrows():
    
    cursor.execute("Insert into [Produtos](ID,Nome,Price,Id_Category)values(?,?,?,?)",linha.ID,linha.Nome,linha.Price,linha.Id_Category) 
     # inserir colunas e quantas colunas tiver passar quantidade de ??
cursor.commit()   # validar dados no SQL Server

# %%
#Carga Categoria
for index, linha in Categoria.iterrows():
    
    cursor.execute("Insert into [Categoria](ID,Categoria)values(?,?)",linha.id,linha.Nome) 
     # inserir colunas e quantas colunas tiver passar quantidade de ??
cursor.commit()   # validar dados no SQL Server

# %%
#Carga Itens 
Itens['total_price'] = Itens['total_price'].astype(float) # conversao de dados

for index, linha in Itens.iterrows():
    
    cursor.execute("Insert into [Items](id,order_id,product_id,quantity,total_price)values(?,?,?,?,?)",linha.id,linha.order_id,linha.product_id,linha.quantity,linha.total_price) 
     # inserir colunas e quantas colunas tiver passar quantidade de ??
cursor.commit()   # validar dados no SQL Server (cuidado com transacoes em aberto)

# %%
#Carga Ordens
for index, linha in Ordens.iterrows():
    
    cursor.execute("Insert into [Ordens](id,created_at,customer_id,status)values(?,?,?,?)",linha.id,linha.created_at,linha.customer_id,linha.status) 
     # inserir colunas e quantas colunas tiver passar quantidade de ??
cursor.commit()   # validar dados no SQL Server

# %%
#Carga Clientes
Clientes['created_at'] = pd.to_datetime(Clientes['created_at'])
Clientes['email'] = Clientes['email'].fillna('Sem registro')
Clientes['street'] = Clientes['street'].fillna('Sem Info')
Clientes['number'] = Clientes['number'].fillna('Sem Numero')
Clientes['additionals'] = Clientes['additionals'].fillna('Sem Info')

for index, linha in Clientes.iterrows():   
    linha.email = str(linha.email)  # Converter para o tipo 'str' antes da inserção
    linha.country = str(linha.country)
    linha.state = str(linha.state)
    linha.street = str(linha.street)
    linha.number = str(linha.number)
    linha.additionals = str(linha.additionals)
    
    #linha.cell_phone = str(linha.cell_phone)
    cursor.execute("INSERT INTO [Clientes] (id, created_at,first_name, last_name,email,cell_phone,country, state,street, number, additionals) VALUES (?,?,?,?,?,?,?,?,?,?,?)",linha.id, linha.created_at,linha.first_name,
                   linha.last_name,linha.email,linha.cell_phone,linha.country,linha.state,linha.street,linha.number,linha.additionals)
cursor.commit()   # validar dados no SQL Server

# %% [markdown]
# Fecha conexão e cursor
# 

# %%

cursor.close()    #Fechar Cursor
conexaoDB.close() #Fechar Conexao


