# %% [markdown]
# # Comando for - Iterando sobre sequências de dados (percorrendo iteráveis)

# %% [markdown]
# ### Iterando sobre uma lista

# %%
lista = [1, 19, 2, 15, 21, 12, 2]
for num in lista:
    print(num)

# %%
print(num)

# %%
# Verificando se um número é par ou ímpar
for num in lista:
    if num % 2 == 0:
        print ("{} é par.".format(num))
    else:
        print(num,"é ímpar.")

# %%
# Contador [impares e pares]
cont_impar = 0
cont_par = 0
for num in lista:
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
print("A lista contem {} números pares e {} números ímpares.".format(cont_par, cont_impar))

# %%
# Somatório
soma = 0
for n in lista:
    soma += n
print("A soma dos elementos da lista = ", soma)

# %%
# Há uma forma mais simples de calcular somatórios
print("A soma dos elementos da lista = ", sum(lista))

# %%
# Mas a função sum() não permite somar elementos específicos
soma_impar = 0
for n in lista:
    if n % 2 == 1:
        soma_impar = soma_impar + n # sompa_impar += n
print("A soma dos elementos ímpares da lista = ", soma_impar)

# %% [markdown]
# ### Iterando sobre uma faixa de valores gerada com a função range()

# %%
# Iterando sobre uma faixa de valores gerada com a função range()
for i in range(5):
    print(i)

# %%
# Somatório dos múltiplos de 3 entre 1 e 100
soma_mult_3 = 0
for x in range(3, 100, 3):
    soma_mult_3 += x
print(soma_mult_3)

# %%
# Imprimindo a taboada de um número qualquer
num = int(input("Digite o número que deseja imprimir a taboada: "))
for mult in range(1,11):
    print("{} x {} = {}".format(num, mult, num*mult))

# %%
# Imprimindo a taboada de 1 a 9
for num in range(1,10):
    for mult in range(1,11):
        print("{} x {} = {}".format(num, mult, num*mult))
    print()

# %% [markdown]
# ### Iterando sobre um string

# %%
maiorpalavra  = "pneumoultramicroscopicossilicovulcanoconiótico"
for letra in maiorpalavra:
    print(letra)

# %% [markdown]
# ### Iterando sobre uma tupla

# %%
tupla = (1, 19, 5, 12, 6)
for ele in tupla:
    print(ele)

# %%
lista_tupla = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
(t1, t2, t3) = lista_tupla[1] # desmembrando a tupla
print(type(lista_tupla))
print(type(lista_tupla[1]))
print(type(t1))

# %%
lista_tupla

# %%
lista_tupla[1]

# %%
t1

# %%
t2

# %%
t3

# %%
lista_tupla_notas = [(18, 20, 15, 22), (10, 15, 25, 19), (16, 24, 21, 20), (10, 13, 18, 13)]
for (ele1, ele2, ele3, ele4) in lista_tupla_notas:
    print("A 3a nota = {}.".format(ele3))

# %% [markdown]
# ### Iterando em um conjunto

# %%
conj1 = {1, 5, 2, 6, 3, 4}

for ele in conj1:
    print(ele)

# %%
conj2 = {1, 17, 12, 4, 2, 20}

for ele in conj1:
    if ele in conj2:
        print("O elemento {} está contido em conj2.".format(ele))
    else:
        print("O elemento {} não está contido em conj2.".format(ele))

# %% [markdown]
# ### Iterando em um dicionário

# %%
dic_estados = { "MG":"Minas Gerais", "PR": "Paraná", "BA": "Bahia", "RN": "Rio Grande do Norte", "AM": "Amzonas"}
for est in dic_estados:
    print(est)

# %%
for est in dic_estados.values():
    print(est)

# %%
for (sig,est) in dic_estados.items():
    print("A sigla para {} é {}.".format(est, sig))

# %% [markdown]
# ### Comprehensions
# 
# Uma maneira bastante concisa que o Python fornece para a criação de sequencias (listas, tuplas, dicionários, strings, etc).
# 
# **Sintaxe:**
# 
# ```python
# listasaida = [expressão for var in listaentrada]
# 
# listasaida = [expressão for var in listaentrada if condição]
# ```
# 
# **Exemplo:**
# 
# Como criar uma lista com 20 elementos (1 a 20) no Python?

# %%
# 1a maneira - digitando todos os elementos
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista

# %%
# 2a maneira - usando a função range
lista1= list(range(1, 21))
lista1

# %%
# 3a maneira - usando o for
lista3 = []
for i in range(1, 21):
    lista3.append(i)
lista3

# %%
# 4a maneira - usando comprehensions
lista4 = [i for i in range(1,21)]
lista4

# %%
# Outro exemplo: criar uma lista de números pares entre 1 e 50
pares = []
for i in range(1, 51):
    if i%2 == 0:
        pares.append(i)
pares

# %%
pares2 = [num for num in range (1,51) if num % 2 == 0]
pares2

# %%
divisiveis3e7 = [num for num in range(1,100) if num % 3 == 0 and num % 7 == 0]
divisiveis3e7

# %%
letras = [l.upper() for l in "palavra"]
letras

# %%



