# %%


# %% [markdown]
# # Indexação e fatiamento (slicing)

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
# ### Acessando elementos específicos

# %%
# Acessando elementos de um ndarray de 1 dimensão
a1D

# %%
# nome_do_array[índice]
a1D[0]

# %%
a1D[2]

# %%
a1D[-1]

# %%
indices = [3, 0, -1] # Definindo uma lista com os índices que se deseja acessar
a1D[indices]

# %%
# Acessando elementos de um ndarray de 2 dimensões
a2D

# %%
# nome_da_matriz[linha][coluna]
a2D[1][2]

# %%
a2D[3][4]

# %%
indice_lin = [0, 1, 2, 3]
indice_col = [0, 1, 2, 3]

a2D[indice_lin, indice_col]

# %%
indice_lin = [0, 1, 2, 3]
indice_col = [3, 2, 1, 0]

a2D[indice_lin, indice_col]

# %%
indice_lin = [3, 2, 1, 0]
indice_col = [3, 2, 1, 0]

a2D[indice_lin, indice_col]

# %%
a2D[:,[0,1,2,0]] 

# %%
a2D[:,[0,1,2,0]][[1, 0, 1, 0]]

# %%
a2D

# %%
a2D[[1, 0, 1, 0]][:,[0,1,2,0]] 

# %%
# Acessando elementos de um ndarray de 3 dimensões
a3D

# %%
# nome_do_cubo[página][linha][coluna]
a3D[2][0][3]

# %%
a3D[0][3][1]

# %% [markdown]
# ### Fatiamento (slicing)

# %%
# Array de 1 dimensão
a1D

# %%
a = a1D[1:5] # Índice 1 ao 4
a

# %%
b = a1D[0:6] # Índice 0 ao 5
b

# %%
c = a1D[:6] # Do início ao 5
c

# %%
d = a1D[::2] # Do início ao fim, com passo 2
d

# %%
e = a1D[-1::-1] # Do final até o início
e

# %%
# Array de 2 dimensões
a2D

# %%
linha0 = a2D[0] # Todos os elementos da linha 0 - outra forma seria: linha0 = a2D[0,:]
linha0

# %%
linha1 = a2D[1,:] # Todos os elementos da linha 1
linha1

# %%
linha2 = a2D[2,1:4] # Linha 2, colunas 1, 2 e 3
linha2

# %%
linha3 = a2D[:][3] # a2D[:] retorna toda a matriz, então de toda a matriz queremos a linha 3 a2D[:][3]
linha3

# %%
coluna2 = a2D[:,2] # De todas as linhas, selecionar a coluna 2
coluna2

# %%
coluna3 = a2D[1:,3] # Da linha um até a última, selecionar a coluna 3
coluna3

# %%
# Array de 3 dimensões
a3D

# %%
# Acessando a página/face 1
face1 = a3D[1]
face1

# %%
# Acessando uma parte da face1
subface1 = a3D[1,0:3, 1:4]
subface1

# %%
linha2face0 = a3D[0,2] # outra forma: linha2face0 = a3D[0,2,:]
linha2face0

# %%
a3D

# %%
linha1todasfaces = a3D[:,1] # outra forma: linha1todasfaces = a3D[:,1,:]
linha1todasfaces

# %%
coluna3todasfaces = a3D[:,:,3]
coluna3todasfaces

# %% [markdown]
# ### Indexação com booleanos

# %%
a2D = np.random.randint(1, 501, (10, 8)) # Cria um ndarray de 4 linhas x 5 colunas com elementos entre 1 e 100
a2D

# %%
a2D >= 250

# %%
a2D[a2D >= 250]

# %%
a2D.mean()

# %%
a2D[a2D <= a2D.mean()]

# %%



