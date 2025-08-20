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
dados = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Produto.xlsx")


# %%
cursor.execute('truncate table [Produtos]')   #executa tarefa de  apagar dados
cursor.commit()

# %%
for index, linha in dados.iterrows():
    
    cursor.execute("Insert into [Produtos](ID,Nome,Price,Id_Category)values(?,?,?,?)",linha.ID,linha.Nome,linha.Price,linha.Id_Category) 
     # inserir colunas e quantas colunas tiver passar quantidade de ??
cursor.commit()   # validar dados no SQL Server
cursor.close()    #Fechar Cursor
conexaoDB.close() #Fechar Conexao


