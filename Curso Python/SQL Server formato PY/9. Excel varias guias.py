# %%
import pandas as pd

# %%
# extração padrão
df = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx") 
display(df)

# %%
# extração selecionando guia espesifica (sheet_name + nome da guia excel)
df = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx" ,sheet_name='Produto (2)' ) 
display(df)

# %%
# extração selecionando guia espesifica (sheet_name + nome da guia excel)
TabelaProduto = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx" , sheet_name= 'Planilha2')
display(TabelaProduto)

# %%
# extração selecionando guia espesifica + pula linha (sheet_name + nome da guia excel + skiprows pula quantas linhas quiser )
#skiprows pula linha
tabelaProduto = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx" , sheet_name= 'Planilha2',skiprows=3)
display(tabelaProduto)

# %%
# escolhendo coluns espefificas (usecols  )
tabelaProduto2 = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx", sheet_name= 'Vendas')
display(tabelaProduto2)

# %%
# escolhendo coluns espefificas (usecols)
produto = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx" , sheet_name= 'Vendas',usecols='A:B')
display(produto)

# %%
# escolhendo coluns espefificas (usecols  )
Loja = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx" , sheet_name= 'Vendas',usecols= 'F:G')
display(Loja)

# %%
# escolhendo coluns espefificas (usecols  )
tabelaProduto2 = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx" , sheet_name= 'Vendas')
display(tabelaProduto2)

# %%
# escolhendo coluns espefificas (usecols)  + usando uma lista 
Produto = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx" , sheet_name= 'Vendas',usecols= [0,1,2])
display(Produto)

# %%
# escolhendo coluns espefificas (usecols)  + usando uma lista 
Loja = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx", sheet_name= 'Vendas',usecols= [5,6,7])
display(Loja)

# %%
# escolhendo coluns espefificas    usecols + skiprows
planilha4 = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx" , sheet_name= 'Planilha4')
display(planilha4)

# %%
# escolhendo coluns espefificas    usecols + skiprows
planilha4 = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx" , sheet_name= "Planilha4",usecols="g:h",skiprows=7)
display(planilha4)

# %%
#skiprows = pula linha 
#nrows = seleciona até a quantidade de linhas que voce quiser
LojaProduto = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx" , sheet_name= 'Produto - Loja')
display(LojaProduto)

# %%
#skiprows = pula linha 
#nrows = seleciona até a quantidade de linhas que voce quiser 
produto = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx" , sheet_name= 'Produto - Loja' , nrows= 11)
display(produto)

# %%
#skiprows = pula linha 
#nrows = seleciona até a quantidade de linhas que voce quiser 
Loja = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx" , sheet_name= 'Produto - Loja' , skiprows= 13)
display(Loja)

# %%
Loja = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx" , sheet_name= 'Produto - Loja' ,usecols='G:H', skiprows=13)
display(Loja)

# %%
Loja = pd.read_excel(r"C:\Users\Admin\Documents\data-engineer-fundamentals-masterclass\data-engineer-fundamentals-masterclass\Origem de dados\arquivos_excel\Caquinha.xlsx", sheet_name= 'Produto - Loja' ,usecols='G:H', nrows=11)
display(Loja)


