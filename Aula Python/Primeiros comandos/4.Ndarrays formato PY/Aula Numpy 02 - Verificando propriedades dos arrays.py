# %% [markdown]
# # Verificando propriedades de um ndarray

# %%
# Importando o NumPy
import numpy as np

# %%
# Cria um ndarray com 10 elementos entre 0 e 9
a1D = np.random.randint(0, 10, 10)
a1D

# %%
a2D = np.random.randint(1, 101, (4,5)) # Cria um ndarray de 4 linhas x 5 colunas com elementos entre 1 e 100
a2D

# %%
a3D = np.random.random((3,4,5)) # Cria um ndarray de 3 páginas x 4 linhas x 5 colunas com elementos entre 0 e 1
a3D

# %% [markdown]
# ### Verificando o formato e quantidade de dimensões de um array - shape e dim

# %%
# A propriedade shape retorna o formato do array
a1D.shape

# %%
a2D.shape

# %%
a3D.shape

# %%
# A propriedade ndim retorna o números de dimensões do array
a1D.ndim

# %%
a2D.ndim

# %%
a3D.ndim

# %% [markdown]
# ### Verificando o tamanho das dimensões de um array - len

# %%
len(a1D) # Retorna o tamanho da 1a dimensão (quantidade de colunas)

# %%
len(a2D) # Retorna o tamanho da 1a dimensão (quantidade de linhas)

# %%
len(a2D[0]) # Retorna o tamanho da 2a dimensão (quantidade de colunas)

# %%
len(a3D) # Retorna o tamanho da 1a dimensão (quantidade de páginas)

# %%
len(a3D[0]) # Retorna o tamanho da 2a dimensão (quantidade de linhas)

# %%
len(a3D[0][0]) # Retorna o tamanho da 3a dimensão (quantidade de colunas)

# %% [markdown]
# ### Verificando a quantidade de elementos de um array - size

# %%
a1D.size

# %%
a2D.size

# %%
a3D.size

# %% [markdown]
# ### Verificando o tipo dos elementos um array - dtype

# %%
a1D.dtype

# %%
a1D.dtype.name

# %%
a2D.dtype

# %%
a2D.dtype.name

# %%
a3D.dtype

# %%
a3D.dtype.name

# %%



