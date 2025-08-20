# %% [markdown]
# # Dicionários
# 
# * Um dicionário é uma coleção de elementos que possuem uma *chave* e um *valor*
# * Ao invés de um índice, usamos a *chave* para recuperar um *valor*
# 
# O que veremos nessa aula:
# 
# 1. Como criar dicionários
# 2. Acessando um valor em um dicionário através de uma chave
# 3. Modificando valores em um dicionário
# 4. Principais métodos de um objeto dicionário

# %%
# fontes
""" 
https://www.w3schools.com/python/python_lists.asp
https://docs.python.org/pt-br/3/tutorial/datastructures.html#more-on-lists



"""

# %% [markdown]
# ### 1. Como criar dicionários

# %%
# Criando dicionários vazios
dic_vazio1 = {}
dic_vazio2 = dict()

# %%
# Visualizando o tipo de dic_vazio1
type(dic_vazio1)

# %%
# Verificando se dic_vazio2 é uma instância de dict
isinstance(dic_vazio2, dict)

# %%
# Criando dicionários com pares chave/valor

# Dicionário de estados: chave é a sigla do estado e valor é o nome completo
dic_estados = { "MG":"Minas Gerais", "PR": "Paraná", "BA": "Bahia", "RN": "Rio Grande do Norte", "AM": "Amzonas"}
# Obs: o nome do estado Amazonas foi digitado errado de forma intencional
dic_estados

# %% [markdown]
# #### OBS: Perceba que as chaves são adicionadas em ordem crescente

# %%
# Dicionário de produtos: chave é o código e valor é a descrição do produto
dic_produtos = {1215:"Lápis", 3221:"Caneta", 2329:"Borracha", 1092:"Caderno", 7633:"Cola"}
dic_produtos

# %%
# Dicionário de alunos: chave é o nome e valor é uma lista com 3 notas do aluno
dic_notas_alunos = {"João":[30, 12, 21], "Maria": [20, 30, 29], "José": [20, 23, 19]}
dic_notas_alunos

# %%
# Dicionário de alunos 2: chave é o nome e valor é um outro dicionário contendo as 3 notas do aluno
dic_notas_alunos2 = {"João": {"nota1": 30, "nota2": 12, "nota3": 21}, 
                     "Maria": {"nota1": 20, "nota2": 30, "nota3": 29}, 
                     "José": {"nota1": 20, "nota2": 23, "nota3": 19}, 
                    }
dic_notas_alunos2

# %% [markdown]
# ### 2. Acessando um valor em um dicionário através de uma chave

# %%
# Acessando o valor associado à chave "PR"
dic_estados["PR"]

# %%
# Acessando o valor associado à chave "MG" dentro de um comando print
print("Eu nasci em "+dic_estados["MG"]+".")

# %%
# Se a chave não existir, é retornado um erro
dic_estados["XYZ"]

# %%
# Acessando o valor associado à chave 2329
dic_produtos[2329]

# %%
# Acessando o valor associado à chave "Maria" no dicionário dic_notas_aluno
nome_aluno = "Maria"
print("As notas de "+nome_aluno+" foram: "+str(dic_notas_alunos[nome_aluno])+".")

# %%
print(nome_aluno+" tirou "+str(dic_notas_alunos[nome_aluno][0])+" pontos na 1a prova.")

# %%
# Acessando a nota da primeira prova do João no dicionário dic_notas_alunos2
dic_notas_alunos2["João"]["nota1"]

# %% [markdown]
# ### 3. Modificando valores em um dicionário

# %%
# Visualizando o dicionário dic_estados
dic_estados

# %%
# Corrigindo o nome do estado Amazonas
dic_estados["AM"] = "Amazonas"
dic_estados

# %%
# Visualizando o dicionário dic_notas_alunos
dic_notas_alunos

# %%
# Alterando a segunda nota de João para 22
dic_notas_alunos["João"][1] = 22
dic_notas_alunos

# %%
# Alterando todas as notas de Maria. 
# Essa alteração não será feita nota a nota, mas atribuindo uma nova lista com as notas corretas
dic_notas_alunos["Maria"] = [25, 20, 22]
dic_notas_alunos

# %%
# Visualizando o dicionário dic_notas_alunos2
dic_notas_alunos2

# %%
# Alterando a terceira nota do José para 25
dic_notas_alunos2["José"]["nota3"] = 25
dic_notas_alunos2

# %% [markdown]
# ### 4. Principais métodos de um objeto dicionário
# 
# Método | Descrição | Exemplo
# :----- | :-------- | :------
# clear  | Apaga todos os elementos de um dicionário | `dic.clear()`
# copy | Retorna uma cópia dos elementos de um dicionário | `dic_copia = dic.copy()`
# fromkeys | Retorna um dicionário a partir de uma sequência de chaves | `exemplo = dic.fromkeys({"k1", "k4", "k5"})`
# get | Retorna o valor associado a uma chave | `dic.get("k1")`
#  |  | `dic.get("k1", 0)`
# items | Retorna uma visão dos pares chave/valor de um dicionário | `dic.items()`
# keys | Retorna uma visão das chaves de um dicionário | `dic.keys()`
# pop | Remove e retorna o elemento associado à chave passada por parâmetro (provoca erro se a chave não existir) | `dic.pop(2)`
# popitem | Remove e retorna o último elemento adicionado ao dicionário | `dic.popitem()`
# setdefault | Retorna o valor associado a uma chave (se a chave existir). Caso não exista, insere a chave com o valor (opcional) no dicionário | `dic.setdefault(2, "dois")`
# update | Adiciona ao dicionário os pares de chave/valor de outro dicionário passado por parâmetro | `dic.update(dic2)`
# values | Retorna uma visão dos valores de um dicionário | `dic.values`

# %%
# Criando um dicionário exemplo
dic_exemplo = {1:"um", 2:"dois", 3:"três", 4:"quatro"}
dic_exemplo

# %% [markdown]
# #### 4.1 - clear()

# %%
# Removendo os elementos de dic_exemplo
dic_exemplo.clear()
dic_exemplo

# %% [markdown]
# #### 4.2 - copy()

# %%
# Redefinido dic_exemplo
dic_exemplo = {1:"um", 2:"dois", 3:"três", 4:"quatro"}
dic_exemplo

# %%
# Criando uma cópia de dic_exemplo usando o método copy()
dic_exemplo2 = dic_exemplo.copy()
dic_exemplo2

# %% [markdown]
# Obs: Isso já foi discutido na aula sobre listas. Se simplesmente atribuirmos dic_exemplo a dic_exemplo2 (**`dic_exemplo2 = dic_exemplo`**), não estaremos copiando seus elementos, mas criando uma referência (ou um apelido).

# %% [markdown]
# #### 4.3 - fromkeys()

# %%
# Criando um novo dicionário a partir da seleção das chaves que desejamos
dic_num_pares = dict.fromkeys([2, 4, 6, 8, 10])
dic_num_pares

# %%
# Se desejarmos atribuir um valor default, basta informar após a lista com as chaves
dic_num_pares = dict.fromkeys([2, 4, 6, 8, 10], "par")
dic_num_pares

# %% [markdown]
# #### 4.4 - get()

# %%
# O método get retorna o valor associado a uma chave
# Visualizando o valor associado à chave 2
dic_exemplo.get(2)

# %% [markdown]
# #### 4.5 - items()

# %%
# Visualizando os pares chave/valor do dicionário 
dic_exemplo.items()

# %% [markdown]
# #### 4.6 - keys()

# %%
# Visualizando as chaves de um dicionário
dic_exemplo.keys()

# %% [markdown]
# #### 4.7 - pop()

# %%
# Removendo o par chave/valor associado à chave 1
dic_exemplo.pop(1)
dic_exemplo

# %%
# Podemos remover e armazenar o valor removido em uma variável
valor = dic_exemplo.pop(4)
dic_exemplo

# %%
# Visualizando o conteúdo armazenado na variável valor
valor

# %% [markdown]
# #### 4.8 - popitem()

# %%
# Removendo o último par chave/valor adicionado ao dicionário
removido = dic_num_pares.popitem()

# %%
# Visualizando o valor removido
removido

# %%
# Visualizando o dicionário após a remoção do último par chave/valor
dic_num_pares

# %% [markdown]
# #### 4.9 - setdefault()

# %%
# Verificando o valor associado à chave "MG"
dic_estados.setdefault("MG")

# %%
# Verificando o valor associado à chave "ES". 
# Como essa chave não existe, ela é adicionada pelo método setdefault ao dicionário com o valor None
dic_estados.setdefault("ES")

# %%
# Visualizando o conteúdo de dic_estados
dic_estados

# %%
# Verificando o valor associado à chave "ES". 
# Como essa chave não existe, ela é adicionada pelo método setdefault ao dicionário. 
# Nesse caso foi passado que o valor "Santa Catarina"
dic_estados.setdefault("SC", "Santa Catarina")

# %%
# Visualizando o conteúdo de dic_estados
dic_estados

# %% [markdown]
# #### 4.10 - update()

# %%
# Definindo o dicionário dic_estados_centro_oeste com alguns dos estados da região Centro Oeste
dic_estados_centro_oeste = {"MS": "Mato Grosso do Sul", "TO": "Tocantins", "GO": "Goiás"}
dic_estados_centro_oeste

# %%
# Adicionando os estados do Centro Oeste ao dicionário dic_estados
dic_estados.update(dic_estados_centro_oeste)
dic_estados

# %% [markdown]
# #### 4.11 - values()

# %%
# Visualizando os valores de um dicionário
dic_estados.values()

# %% [markdown]
# #### Como remover o estado de Tocantins do dicionário Centro Oeste?

# %%
# Numa primeira versão desse Notebook, o exemplo do pop() seria a remoção do estado de Tocantins, 
# que não faz parte da região Centro-Oeste, mas da região Norte. Para removermos Tocantins do dicionário,
# usamos então o método pop(), passando por parâmetro a sigla do estado "TO"
dic_estados_centro_oeste.pop("TO")


