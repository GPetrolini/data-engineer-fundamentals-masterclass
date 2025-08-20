# %% [markdown]
# https://docs.python.org/pt-br/3/tutorial/datastructures.html  Estruturas de dados

# %% [markdown]
# # Listas
# 
# * Lista é uma coleção de elementos 
# * Cada elemento possui uma posição dentro de uma lista. Essa posição é chamada índice
# * O primeiro elemento fica armazenado na posição *0*, enquanto o último elemento fica armazenado na posição *n-1* (onde *n* é a quantidade de elementos da lista)
# 

# %% [markdown]
# ### 1. Como criar uma lista

# %%
# Criando uma lista vazia
lista_vazia = [25,30]
lista_vazia2 = list()

# %%
# Visualizando o tipo
type(lista_vazia)

# %%
# Visualizando o tipo
type(lista_vazia2)

# %%
# Verificando o tamanho da lista quantidade de linhas 
len(lista_vazia)

# %%
# Criando listas com elementos
lista = [23, 56, 2, -3, 10, 2, 18, 0, 5]
lista_reais = [1.5, -2.13, 5.14]
lista_strings = ["Gustavo", "São Paulo", "Brasil", "Mundo"]
lista_booleanos = [True, True, False, True]
lista_misturada = [1, 2, 3.14159, "teste"]
lista_misturada2 = [1, 2, 3.14159, "teste", [1, "A", 1.0]]
listas_aninhadas = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]

# %%
# Visualizando a lista
lista

# %%
lista_reais

# %%
lista_strings

# %%
print(lista_booleanos)

# %%
lista_misturada

# %%
lista_misturada2

# %%
listas_aninhadas

# %% [markdown]
# ### 2. Como acessar elementos de uma lista

# %%
# Criando listas com elementos
lista = [23, 56, 20, -3, 10, 2, 18, 0, 5]
lista_reais = [1.5, -2.13, 5.14]
lista_strings = ["Gustavo", "São Paulo", "Brasil", "Mundo"]
lista_booleanos = [True, True, False, True]
lista_misturada = [1, 2, 3.14159, "teste"]
lista_misturada2 = [1, 2, 3.14159, "teste", [1, "A", 1.0]]
listas_aninhadas = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]

# %%
# Acessando o índice 0 (primeira posição)
lista[3]

# %%
lista

# %%
# Acessando o índice 2 (terceira posição)
lista[2]

# %%
# Acessando o índice 3 (quarta posição)
lista_strings[0]

# %%
lista_strings

# %%
# Acessando o índice 3 (quarta posição)
lista_misturada[3]

# %%
lista_misturada

# %%

lista_misturada2 = [1, 2, 3.14159, "teste", [1, "A", 1.0]]


# %%
# Acessando o índice 4 nos foi retornado uma lista com 3 elementos. Agora queremos acessar o índice 1 dessa lista interna
lista_misturada2[4][2]

# %%
lista_misturada2

# %%
# Acessando um índice inexistente
lista[2]

# %% [markdown]
# ### 3. Como modificar elementos de uma lista

# %%
# Criando listas com elementos
lista = [23, 56, 20, -3, 10, 2, 18, 0, 5]
lista_reais = [1.5, -2.13, 5.14]
lista_strings = ["Gustavo", "São Paulo", "Brasil", "Mundo"]
lista_booleanos = [True, True, False, True]
lista_misturada = [1, 2, 3.14159, "teste"]
lista_misturada2 = [1, 2, 3.14159, "teste", [1, "A", 1.0]]
listas_aninhadas = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]

# %%
# Visualizando a lista
lista

# %%
# Alterando o elemento do índice 1 de 56 para 18
lista[1] = 18

# %%
# Visualizando a alteração realizada
lista

# %%
# Modificando o elemento do índice 3 de -3 para 15
lista[3] = 15

# %%
# Visualizando a alteração realizada
lista

# %%
# Modificando o elemento do índice 2. Ele recebe a soma dos dois elementos anteriores
lista[2] = lista[0] + lista[1]

# %%
# Visualizando a alteração realizada
lista

# %% [markdown]
# ### 4. Principais métodos de um objeto lista
# 
# Método | Descrição | Exemplo
# :----- | :-------- | :------
# append | Adiciona um elemento no final da lista | `lista.append(5)`
# clear  | Apaga todos os elementos de uma lista | `lista.clear()`
# copy | Retorna uma cópia dos elementos da lista | `copia = lista.copy()`
# count | Retorna a quantidade de ocorrências de um elemento na lista | `qt = lista.count(5)`
# extend | Adiciona os elementos de outra lista passada por parâmetro | `lista.extend(outra_lista)`
# index | Retorna o índice do elemento passado por parâmetro (primeira posição) | `pos5 = lista.index(5)`
# insert | Adiciona um elemento em uma posição passada por parâmetro (adiciona no final caso a posição não exista)| `lista.insert(3, "João")`
# pop | Remove o elemento na posição passada por parâmetro (provoca um erro caso a posição não exista)| `elemento = lista.pop(3)`
# remove | Remove o elemento passado por parâmetro (provoca um erro caso o elemento não exista)| `lista.remove(5)`
# reverse | Inverte a ordem dos elementos de uma lista | `lista.reverse()`
# sort | Ordena os objetos de uma lista | `lista.sort()`
#  | | `lista.sort(reverse=True)`

# %% [markdown]
# #### 4.1 - append()

# %%
# Visualizando a lista antes da chamada ao método append()
lista

# %%
# Adicionado o 17 no final da lista
lista.append(17)

# %%
# Visualizando a lista após chamada ao método append()
lista

# %% [markdown]
# #### 4.2 - clear()

# %%
# Visualizando lista_reais antes da chamada ao método clear()
lista_reais

# %%
# Removendo todos os ementos de lista_reais
lista_reais.clear()

# %%
# Visualizando lista_reais após chamada ao método clear()
lista_reais

# %% [markdown]
# #### 4.3 - copy()

# %%

copia = lista # neste caso estou atribuindo somente um novo nome a lista

# %%
# Visualizando o conteúdo de copia
copia

# %%
# Alterando o elemento do índice 0 de 23 para 5
copia[0] = 5

# %%
# Visualizando o conteúdo de copia
copia

# %%
# Visualizando o conteúdo de lista (Perceba que o elemento 23 também foi alterado na lista, e não apenas em copia)
lista

# %%
# Desfazendo a alteração no índice 0, modificando de 5 para 23
lista[0] = 23

# %%
# A maneira correta de copiar uma lista para outra é através da chamada ao método copy()
copia = lista.copy()   # desta forma eu crio uma cópia e ficam 2 listas separadas idependentes

# %%
# Visualizando o conteúdo de lista
lista

# %%
# Visualizando o conteúdo de copia
copia

# %%
# Alterando o elemento do índice 0 de 23 para 5
copia[0] = 5

# %%
# Visualizando o conteúdo de lista
lista

# %%
# Visualizando o conteúdo de lista - Agora sim, apenas o índice 0 de copia foi alterado
copia

# %% [markdown]
# #### 4.4 - count()

# %%
# Verificando quantas vezes o número 5 aparece em copia
copia.count(5)

# %% [markdown]
# #### 4.5 - extend()

# %%
# Suponha que temos uma lista chamada numeros que contém os elementos [1, 2, 3]
numeros = [1, 2, 3]

# %%
# Queremos adicionar o elementos [4, 5] à lista números e usamos o método append()
numeros.append([4,5])

# %%
# Ao invés de adicionarmos os elementos 4 e 5, adicionar uma lista contendo os elementos [4, 5]
numeros

# %%
# A maneira correta de adicionar novos elementos de uma lista, a partir de outra lista, é através do método extend()
numeros = [1, 2, 3]
numeros.extend([4,5])
numeros

# %% [markdown]
# #### 4.6 - index()

# %%
# Redefinindo os elementos da lista
lista = [1, 3, 7, 2, 3, 8, 4]

# %%
# O método index nos permite saber em que posição determinado elemento está armazenado
lista.index(7)

# %%
# Podemos guardar esse valor em uma variável
posicao8 = lista.index(8)

# %%
posicao8

# %%
# O método index() retorna a posição da primeira ocorrência do elemento procurado. 
posicao3 = lista.index(3)

# %%
posicao3

# %%
# Caso o elemento não exista, ocorre um erro
lista.index(20)

# %% [markdown]
# #### 4.7 - insert()

# %%
# O método insert() permite adicionar um elemento em qualquer posição da lista. 
# Caso a posição não exista, ele insere o elemento desejado na última posição
lista.insert(2, "ABC")
lista

# %%
lista.insert(80, "XYZ") # caso nao exista a posição ele adicina na ultima posicao da lista
lista

# %% [markdown]
# #### 4.8 - pop()

# %%
# Utilizamos o método pop() quando desejamos apagar uma posição da lista
# Removendo o elemento no índice 2
valor = lista.pop(2)
# Visualizando o valor retornado
valor

# %%
# Visualizando a lista após a remoção 
lista

# %%
# Removendo o elemento da última posição
lista.pop(-1)
# Visualizando a lista após a remoção 
lista

# %%
# O método pop() provoca um erro caso a posição não exista
lista.pop(45)

# %% [markdown]
# #### 4.9 - remove()

# %%
# Utilizamos o método remove() quando desejamos apagar um elemento específico da lista
# Visualizando lista_strings antes da remoção
lista_strings

# %%
# Removendo "Rodrigo"
lista_strings.remove("Gustavo")

# %%
# Visualizando lista_strings após a remoção
lista_strings

# %%
# O método remove() provoca um erro caso o elemento não exista
lista_strings.remove("China")

# %% [markdown]
# #### 4.10 - reverse()

# %%
# Redefinindo os elementos de lista
lista = [1, 2, 3, 4, 5, 6]
# Visualizando a lista antes da chamada ao método reverse()
lista

# %%
# Invertendo os elementos da lista
lista.reverse()

# %%
# Visualizando a lista após chamada ao método reverse()
lista

# %% [markdown]
# #### 4.11 - sort()

# %%
# Redefinindo os elementos de lista
lista = [6, 3, 1, 4, 2, 5]
# Visualizando a lista antes da chamada ao método sort()
lista

# %%
# Ordenando os elementos em ordem crescente
lista.sort()

# %%
# Visualizando a lista após chamada ao método sort()
lista

# %%
# Redefinindo os elementos de lista
lista = [6, 3, 1, 4, 2, 5]
# Visualizando a lista antes da chamada ao método sort()
lista

# %%
# Ordenando os elementos em ordem decrescente
lista.sort(reverse=True)

# %%
# Visualizando a lista após chamada ao método sort()
lista

# %%
# Ordenando lista de caracteres
lista_letras = ["Q", "W", "E", "R", "T", "Y", "A", "S", "D"]
lista_letras.sort()
lista_letras

# %%
# Ordenando lista de strings
lista_strings = ["GHI", "XYZ", "DEF", "ABC", "KLM"]
lista_strings.sort()
lista_strings

# %%
# Não é possível ordenar uma lista com elementos de diferentes tipos
lista_misturada = [2, "ABC", 3.14]
lista_misturada.sort()
lista_misturada

# %% [markdown]
# ### 5. Funções aplicáveis a uma lista
# 
# Função | Descrição | Exemplo
# :----- | :-------- | :------
# len | Retorna a quantidade de elementos de uma lista | `print(len(lista))`
# max  | Retorna o maior elemento de uma lista | `maior = max(lista)`
# min | Retorna o menor elemento de uma lista | `menor = min(lista)`
# sum | Retorna o somatório dos elementos de uma lista | `soma = sum(lista)`

# %%
# Redefinindo os elementos de lista e lista_letras
lista = [8, 3, 21, 14, 2, 45]
lista_letras = ["Q", "W", "E", "R", "T", "Y", "A", "S", "D"]

# %%
# A função len() retorna a quantidade de elementos de uma lista
len(lista)

# %%
# A função max() retorna o maior elemento de uma lista
max(lista)

# %%
max(lista_letras)

# %%
# A função min() retorna o menor elemento de uma lista
min(lista)

# %%
min(lista_letras)

# %%
# A função sum() retorna a soma dos elementos de uma lista numérica
sum(lista)


