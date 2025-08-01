# %% [markdown]
# # Conjuntos
# 
# * Conjuntos são coleções de elementos únicos
# * Principais características:
#    * Os elementos não são armazenados em uma ordem específica
#    * Conjuntos não contém elementos repetidos
# * Conjuntos não suportam indexação como as listas e tuplas
# 
# O que veremos nessa aula:
# 1. Como criar conjuntos
# 2. Como acessar elementos de um conjunto
# 3. Como modificar elementos de um conjunto
# 4. Principais métodos de um objeto conjunto
# 5. Funções aplicáveis a um conjunto
# 6. Curiosidade (conversão de uma lista em um conjunto)

# %% [markdown]
# ### 1. Como criar conjuntos

# %%
# Criando conjuntos vazios
conj_vazio1 = set() # Essa é a única forma de se criar um conjunto vazio
conj_vazio2 = {} # As chaves são utilizadas para construir um dicionário vazio.

# %%
type(conj_vazio1)

# %%
type(conj_vazio2)

# %%
# Criando conjuntos com elementos
conj1 = {1, 2, 3, 4, 5}
conj2 = {"A", "B", "C", "D"}
conj3 = {"ABC", 123, 3.14}

# %%
# Conjuntos não podem conter outras estruturas aninhadas
conj3 = {1, "ABC", [1,2,3]} # Provoca um erro por causa da lista

# %% [markdown]
# ### 2. Como acessar elementos de um conjunto

# %%
# Conjuntos não suportam indexação. Então vamos precisar do comando for para acessar os elementos de um conjunto
for elem in conj1:
    print(elem)

# %%
# Tentar acessar uma posição em um conjunto provoca um erro
conj1[0]

# %% [markdown]
# ### 3. Como modificar elementos de um conjunto

# %%
# Nâo existe uma maneira de modificar elementos em um conjunto. 
# O que pode ser feito é a exclusão de um elemento, seguida da inserção de outro elemento

# %% [markdown]
# ### 4. Principais métodos de um objeto conjunto
# 
# Método | Descrição | Exemplo
# :----- | :-------- | :------
# add | Adiciona um elemento ao conjunto | `conj1.add(5)`
# clear  | Apaga todos os elementos de um conjunto | `conj1.clear()`
# copy | Retorna uma cópia dos elementos de um conjunto | `conj_copia = conj1.copy()`
# difference | Retorna o conjunto de elementos de conj1 que não pertencem a conj2 | `conj1.difference(conj2)`
# intersection | Retorna o conjunto de elementos presentes tanto em conj1 quanto em conj2 | `conj1.intersection(conj2)`
# isdisjoint | Retorna True se conj1 e conj2 forem disjuntos (ou seja, não possuem elementos em comum) | `conj1.isdisjoint(conj2)`
# issubset | Retorna True se conj1 for um subconjunto de conj2 (conj1 está contido em conj2) | `conj1.issubset(conj2)`
# issuperset | Retorna True se conj1 for um superconjunto de conj2 (conj1 contém conj2) | `conj1.issuperset(conj2)`
# remove e discard| Removem um elemento do conjunto | `conj1.remove(5)` ou `conj1.discard(5)`
# symmetric_difference | Retorna o conjunto de elementos que não são comuns aos dois conjuntos (o contrário da interseção)| `conj1.symmetric_difference(conj2)`
# union | Retorna a união entre 2 conjuntos | `conj1.union(conj2)`

# %% [markdown]
# #### 4.1 - add()

# %%
# Visualizando os elementos de conj1
conj1

# %%
# Adicionando o elemento 6
conj1.add(6)
conj1

# %% [markdown]
# #### 4.2 - clear()

# %%
# Visualizando os elementos de conj3
conj3

# %%
conj3.clear()
conj3

# %% [markdown]
# #### 4.3 - copy()

# %%
conj3 = conj1.copy()
conj3

# %% [markdown]
# #### 4.4 - difference()

# %%
# Criando os conjuntos s1 e s2
s1 = {1,2,3,4,5}
s2 = {4,5,6,7}

# %%
# Atribui a s3 a diferença do conjunto s1 em relação a s2
s3 = s1.difference(s2)
s3

# %% [markdown]
# #### 4.5 - intersection()

# %%
s4 = s1.intersection(s2)
s4

# %% [markdown]
# #### 4.6 - isdisjoint()

# %%
# Verificando se s1 e s2 são disjuntos
s1.isdisjoint(s2)

# %%
# Verificando se s3 e s3 são disjuntos
s3.isdisjoint(s4)

# %% [markdown]
# #### 4.7 - issubset()

# %%
# verificando se s1 é um subconjunto de s2
s1.issubset(s2)

# %%
# verificando se s3 é um subconjunto de s1
s3.issubset(s1)

# %% [markdown]
# #### 4.8 - issuperset()

# %%
# verificando se s1 é um superconjunto de s2
s1.issuperset(s2)

# %%
# verificando se s1 é um superconjunto de s3
s1.issuperset(s3)

# %% [markdown]
# #### 4.9 - remove() e discard()

# %%
# Visualizando os elementos de conj1
conj1

# %%
# Removendo o 3 de conj1 usando o remove()
conj1.remove(3)

# %%
# Visualizando os elementos de conj1 após remove(3)
conj1

# %%
# Tentar remover um elemento inexistente com remove provoca um erro
conj1.remove(7)

# %%
# Removendo o 6 de conj1 usando o discard()
conj1.discard(6)

# %%
# Visualizando os elementos de conj1 após discard(6)
conj1

# %%
# Tentar remover um elemento inexistente com discard NÃO provoca um erro
conj1.discard(7)

# %% [markdown]
# #### 4.10 - symmetric_difference()

# %%
# Na seção 4.5 foi realizada a interseção de s1 e s2. Agora vamos calcular a diferença simétrica
s5 = s1.symmetric_difference(s2)
s5

# %% [markdown]
# #### 4.11 - union()

# %%
# Calculando o conjunto união. Veja que elementos repetidos só aparecem uma única vez no conjunto resultante
s6 = s1.union(s2)
s6

# %% [markdown]
# ### 5. Funções aplicáveis a um conjunto

# %%
len(s1)

# %%
max(s1)

# %%
min(s1)

# %%
sum(s1)

# %% [markdown]
# ### 6. Curiosidade (conversão de uma lista em um conjunto)

# %%
# O que acontece se convertermos uma lista que contém elementos repetidos em um conjunto?
lista = [1, 2, 4, 3, 2, 1, 5, 2, 3, 1, 6, 3, 4, 2]

# %%
# Convertendo a lista em um conjunto
conj_lista = set(lista)

# %%
# Ao visualizar o conjunto obtido através da conversão da lista, vemos que não existem mais elementos repetidos
conj_lista


