# %% [markdown]
# # Tuplas
# 
# * Assim com uma lista, uma tupla também é uma coleção de elementos. A diferença entre elas, é que a tupla é imutável. Ou seja, uma vez definidos os seus elementos, a tupla não pode mais ser alterada
# * Cada elemento possui uma posição dentro de uma lista. Essa posição é chamada índice
# * O primeiro elemento fica armazenado na posição *0*, enquanto o último elemento fica armazenado na posição *n-1* (onde *n* é a quantidade de elementos da lista)
# 
# O que veremos nessa aula:
# 
# 1. Como criar uma tupla
# 2. Como acessar elementos de uma tupla
# 3. A imutabilidade de uma tupla
# 4. Principais métodos de um objeto tupla
# 5. Funções aplicáveis a uma tupla
# 6. Convertendo uma tupla em lista

# %% [markdown]
# ### 1. Como criar uma tupla

# %%
# Criando tuplas vazias
tupla_vazia = ()
tupla_vazia2 = tuple()

# %%
# Verificando o tipo de tupla_vazia
type(tupla_vazia)

# %%
# Verificando se tupla_vazia2 é uma instância de tuple
isinstance(tupla_vazia2, tuple)

# %%
len(tupla_vazia)

# %%
# Criando tuplas com elementos
tupla1 = (3, 19, 4, 21, 3, 5, 13)
tupla2 = (3, 19, 4, 21, 3, 5, 13, "tupla", (1, 2, 3))
tupla3 = (3, 19, 4, 21, 3, 5, 13, "tupla", [1, 2, 3])

# %%
# Visualizando os elementos de tupla1
tupla1

# %%
# Visualizando os elementos de tupla2
tupla2

# %%
# Visualizando os elementos de tupla3
tupla3

# %% [markdown]
# ### 2. Como acessar elementos de uma tupla

# %%
# Acessando o índice 0 (primeira posição) de tupla1
tupla1[0]

# %%
# Visualizando os elementos de tupla1
tupla1

# %%
# Acessando o índice 5 (sexta posição) de tupla2
tupla2[5]

# %%
# Visualizando os elementos de tupla2
tupla2

# %%
# Acessando o índice 8 (nona posição) de tupla3
tupla3[8]

# %%
# Visualizando os elementos de tupla3
tupla3

# %%
# Tentando acesso a um índice inexistente
tupla3[20]

# %% [markdown]
# ### 3. A imutabilidade de uma tupla

# %%
# Atribuindo o valor 5 ao índice 0 de tupla1 provocará um erro
tupla1[0] = 5

# %%
# O mesmo ocorre se tentarmos atribuir o string "imutável" para o índice 1 de tupla2 
tupla2[1] = "imutável"

# %%
# O índice 8 de tupla2 contém uma outra tupla contendo 3 valores (1, 2, 3).
# Tentar atribuir 5 ao índice 1 dessa tupla interna, provocará um erro de execução
tupla2[8][1] = 5

# %%
# O mesmo não ocorre ao tentar atribuir 5 ao índice 1, da lista armazenada no índice 8. 
# O motivo é que a tupla não está sendo alterada. O índice 8 continua contendo uma lista. 
# Essa lista, por sua vez, é que teve um de seus valores alterados
tupla3[8][1] = 5

# %%
# Podemos adicionar elementos à lista armazenada no índice 8 da tupla
tupla3[8].extend([4, 5, 6])

# %%
tupla3

# %%
# Entretanto, matendo a característica de imutabilidade, não podemos substituir a lista do índice 8 por outra
tupla3[8] = [-1, -2, -3]

# %% [markdown]
# ### 4. Principais métodos de um objeto tupla

# %%
# Verificando quantas vezes o número 3 aparece em tupla1
tupla1.count(3)

# %%
tupla1

# %%
# Verificando em que posição está armazenado o elemento 21
tupla1.index(21)

# %% [markdown]
# ### 5. Funções aplicáveis a uma tupla

# %%
len(tupla1)

# %%
max(tupla1)

# %%
min(tupla1)

# %%
sum(tupla1)

# %% [markdown]
# ### 6. Convertendo uma tupla em lista

# %%
lista = list(tupla1)

# %%
lista

# %%
tupla1[6] = -1 # A imutabilidade da tupla não permite a alteração de um valor

# %%
lista[6] = -1 # A lista resultante da conversão da lista permite a alteração

# %%
lista


