# %% [markdown]
# # NumPy - Numerical Python
# 
# ## Criando arrays NumPy

# %%
# Importando o NumPy
import numpy as np

# %% [markdown]
# ### Criando arrays de 1 dimensão

# %%
a1D = np.array([1, 2, 3])
a1D

# %%
# O objeto criado é um ndarray: n-dimensional array
type(a1D)

# %%
# Verificando o tipo dos elementos
a1D.dtype

# %%
b1D = np.array([1, 2, 3], dtype = float)
b1D

# %%
b1D.dtype

# %%
c1D = np.array([1, 2, 3], dtype = str)
c1D

# %%
# str > float > int > bool
d1D = np.array([1, 3.14, "NumPy", True])
d1D

# %%
e1D = np.array([1, 3.14, False, True])
e1D

# %%
e1D.dtype

# %%
f1D = np.array([1, False, True])
f1D

# %%
f1D.dtype

# %%
g1D = np.array([False, True])
g1D

# %%
g1D.dtype

# %% [markdown]
# ### Criando arrays de 2 dimensões

# %%
a2D = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9]])
a2D

# %%
a2D.dtype

# %% [markdown]
# ### Criando arrays de 3 dimensões

# %%
a3D = np.array( [ [ [1,2,3], [4,5,6], [7,8,9] ], [ [11,12,13], [14,15,16], [17,18,19] ], [ [21,22,23], [24,25,26], [27,28,29] ]])
a3D

# %% [markdown]
# ## Outras formas de criar arrays
# 
# ### Arrays preenchidos com zeros - zeros()

# %%
# 1 dimensão
azeros = np.zeros(5)
azeros

# %%
# 2 dimensões
bzeros = np.zeros((3, 4)) # 3 linhas e 4 colunas
bzeros

# %%
# 3 dimensões
czeros = np.zeros((3, 4, 2)) # 3 páginas, 4 linhas e 2 colunas
czeros

# %%
# 2 dimensões
dzeros = np.zeros((3, 4), dtype = int) # 3 linhas e 4 colunas
dzeros

# %% [markdown]
# ### Arrays preenchidos com 1's - ones()

# %%
# 1 dimensão
a_um_1D = np.ones(5)
a_um_1D

# %%
b_um_1D = np.ones(10, dtype = str)
b_um_1D

# %%
c_um_1D = np.ones(5, dtype = int)
c_um_1D

# %%
# 2 dimensões
d_um_2D = np.ones((4, 3)) # 4 linhas e 3 colunas
d_um_2D

# %%
# 3 dimensões
e_um_3D = np.ones((5, 2, 3)) 
e_um_3D

# %%
# 4 dimensões
f_um_4D = np.ones((3, 4, 2, 3)) 
f_um_4D

# %% [markdown]
# ### Arrays preenchidos com faixas de valores - arange()

# %%
# Cria um ndarray preenchido com  os elementos de 0 a n-1
# No exemplo abaixo vai criar um ndarray com os elementos 0 a 9
a1D = np.arange(10)
a1D

# %%
# Cria um ndarray preenchido com os elementos variando entre o valor inicial e o valor final - 1
# Nesse exemplo vai criar um array com os elementos de 5 a 14
b1D = np.arange(5, 15)
b1D

# %%
# Cria um ndarray preenchido com os elementos variando entre o valor inicial e o valor final - 1, com um determinado step
# No exemplo vai criar um array com os elementos de 5 a 100, com passo 10. Ou seja: 5, 15, 25...95
c1D = np.arange(5,100, 10)
c1D

# %% [markdown]
# ### Criando arrays preenchidos com valores igualmente espaçados - linspace()

# %%
# Cria um array com n elementos entre o valor inicial e valor final, igualmente espaçados
d1D = np.linspace(0,10, 2) # Cria um array com 2 valores entre 0 e 10
d1D

# %%
e1D = np.linspace(0,10, 4) # Cria um array com 2 valores entre 0 e 10
e1D

# %%
f1D = np.linspace(1,1000) # Se não for passada a quantidade de elementos, o padrão é gerar 50 elementos
f1D

# %%
g1D = np.linspace(1,1000, dtype = int) # gerando int, a função simplesmente corta as casas decimais
g1D

# %%
h1D = np.linspace(0,50, 10, endpoint = True) # O valor final é incluído
h1D


# %%
i1D = np.linspace(0,50, 10, endpoint = False) # O valor final não é incluído
i1D

# %% [markdown]
# ### Criando arrays preenchidos com um único valor passado por parâmetro - full()

# %%
a1D = np.full(10, 5) # ndarray contendo 10 números 5
a1D

# %%
a2D = np.full((3, 5), 3)  # ndarray de 3 linhas e 5 colunas contendo o número 3
a2D

# %%
a3D = np.full((3, 5, 8), -1)  # ndarray de 3 páginas, 5 linhas e 8 colunas contendo o número -1
a3D

# %% [markdown]
# ### Criando matriz identidade - eye()

# %%
ident = np.eye(5) # Cria uma matriz 5x5 preenchida com 1s na diagonal principal e 0 nas posições restantes
ident

# %% [markdown]
# ### Criando matriz com elementos aleatórios

# %%
a1D = np.random.randint(0, 100, 10) # Cria um ndarray com 10 elementos entre 0 e 99
a1D

# %%
a2D = np.random.randint(1, 500, (4,5))
a2D

# %%
# Gerando 10 combinações para a mega-sena
# Valores vão de 1 a 60, 10 páginas, 1 linha, 6 colunas
a3D = np.random.randint(1,61,(10,1,6)) 
a3D

# %%
b1D = np.random.random(10) # Cria um ndarray contendo 10 elementos aleatórios entre 0 e 1
b1D

# %%
c2D = np.random.random((4,5)) # Cria um ndarray de 4 linhas e 5 colunas contendo elementos aleatórios entre 0 e 1
c2D

# %%



