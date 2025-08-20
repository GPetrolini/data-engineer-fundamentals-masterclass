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
Categoria= pd.read_sql('select * from categoria',conexaoDB)
Categoria.head()

# %%
Query='select * from categoria'
Categoria2=pd.read_sql(Query,conexaoDB)
Categoria2.head()


