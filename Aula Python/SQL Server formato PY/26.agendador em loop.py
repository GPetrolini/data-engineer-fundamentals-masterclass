# %% [markdown]
# https://schedule.readthedocs.io/en/stable/

# %%
# pip install schedule
# pip install -- upgrade schedule

# %%
import schedule  # Importa agendamento de tarefas
import time  # Importa a biblioteca 'time' para pausas de tempo


def job():                      # def = uma função depois de o nome dessa função
    print("estou funcionando")  # Imprime uma mensagem indicando (Trocar pelo seu script)
    
# Agendando tarefas com diferentes intervalos e horários
schedule.every(10).minutes.do(job)                              # Executa a cada 10 minutos
schedule.every().hour.do(job)                                   # Executa a cada hora
schedule.every().day.at("10:30").do(job)                        # Executa diariamente às 10:30
schedule.every().monday.do(job)                                 # Executa toda segunda-feira
schedule.every().wednesday.at("13:15").do(job)                  # Executa toda quarta-feira às 13:15
schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)    # Executa diariamente às 12:42 (usando fuso horário Europe/Amsterdam)
schedule.every().day.at("12:42").do(job)                        # Executa diariamente às 12:42 (usando fuso horário Seu PC)
schedule.every().minute.at(":17").do(job)                       # Executa' a cada minuto quando o segundo é 17

# Executar as tarefas agendadas em um loop contínuo

while True: # loop contínuo
    schedule.run_pending()  # Executa tarefas agendadas que estão prontas para serem executadas
    time.sleep(1)  # Pausa por 1 segundo antes de verificar novamente as tarefas agendadas(em segundos )


# %%
schedule.clear()  # limpar todas as jobs
## intenroperno CMD ou Terminal 
# Ctrl + \
# Ctrl + C

# %% [markdown]
# Exemplo pratico

# %%
import schedule  
import time  


def job():                      # def = uma função depois de o nome dessa função
    
    print("Estou funcionando teste Final")  # Colar meu script dando a identação (Tab)
    
    
schedule.every(1).seconds.do(job) 
while True: # loop contínuo
    schedule.run_pending()  # Executa tarefas agendadas que estão prontas para serem executadas
    time.sleep(1)  # Pausa por 1 segundo antes de verificar novamente as tarefas agendadas     
    

# %%
schedule.clear()  # limpar todas as jobs

# %%
import schedule  
import time  
import pandas as pd
import pyodbc 



def job():  
    server = 'DESKTOP-33OODCPL' 
    database = 'Python' 
    conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        f'SERVER={server};'
                        f'DATABASE={database};'
                        'Trusted_Connection=yes;')

    cursor = conexaoDB.cursor()   # criando cursor de comando 

    dados = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Categoria.xlsx")
    str(dados.columns).replace("'","") 

    # faz carga no banco de dados
    for index, linha in dados.iterrows():
        
        cursor.execute("Insert into [Categoria](ID,Categoria)values(?,?)",linha.id,linha.Nome) 
        
    cursor.commit()   
    cursor.close() 
    conexaoDB.close() 
    
schedule.every(10).seconds.do(job) # escolher a frequencia 
while True: # loop contínuo
    schedule.run_pending()  # Executa tarefas agendadas que estão prontas para serem executadas
    time.sleep(1)  # Pausa por 1 segundo antes de verificar novamente as tarefas agendadas   
    

# %% [markdown]
# Script em um bloco

# %%

import pandas as pd
import pyodbc 

server = 'DESKTOP-33OODCPL' 
database = 'Python' 
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      f'SERVER={server};'
                      f'DATABASE={database};'
                      'Trusted_Connection=yes;')

cursor = conexaoDB.cursor()   # criando cursor de comando 

dados = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Categoria.xlsx")
str(dados.columns).replace("'","") 

#limpa banco de dados antes da carga 
cursor.execute('truncate table [Categoria]')  
cursor.commit()

# faz carga no banco de dados
for index, linha in dados.iterrows():
    
    cursor.execute("Insert into [Categoria](ID,Categoria)values(?,?)",linha.id,linha.Nome) 
     
cursor.commit()   
cursor.close() 
conexaoDB.close() 


