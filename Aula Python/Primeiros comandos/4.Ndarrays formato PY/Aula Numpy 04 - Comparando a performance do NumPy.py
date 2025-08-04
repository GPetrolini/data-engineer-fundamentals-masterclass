# %% [markdown]
# # Comparação da performance do NumPy

# %%
idades = [18, 41, 13, 25, 2, 10]

# %%
# Somando todos os elementos com uma função
def soma(numeros):
    soma = 0
    for num in numeros:
        soma = soma + num
    return soma

# %%
# Somar as idades usando a função soma
soma(idades)

# %%
# Somar as idades usando a função sum() do Python
sum(idades)

# %%
# Somar as idades usando a função np.sum() do Python
import numpy as np
np.sum(idades)

# %%
# Gerando uma quantidade maior de elementos
idades = np.random.randint(0, 50, 20000000)
len(idades)

# %%
print(soma(idades))
print(sum(idades))
print(np.sum(idades))

# %%
#%timeit soma(idades)

# %%
#%timeit sum(idades)

# %%
#%timeit np.sum(idades)

# %% [markdown]
# ### Calculando o quadrado de cada número

# %%
numeros = np.random.randint(0, 50, 10000000)
# Usando uma função iterativa (num * num)
def quadrado(numeros):
    quadrados = []
    for num in numeros:
        quadrados.append(num * num)
    return quadrados

#%timeit quadrado(numeros)

# %%
# Usando uma função iterativa (num ** 2)
def quadrado2(numeros):
    quadrados = []
    for num in numeros:
        quadrados.append(num ** 2)
    return quadrados

#%timeit quadrado2(numeros)

# %%
# Usando comprehension
def quad_comprehension(numeros):
    return [num * num for num in numeros]

#%timeit quad_comprehension(numeros)

# %%
# Usando map()
def quad_map(numeros):
    return list(map(lambda num: num * num, numeros))

#%timeit quad_map(numeros)

# %%
# Usando o NumPy
#%timeit np.power(numeros,2)

# %%
# Usando o NumPy - convertendo para list
#%timeit list(np.power(numeros,2))

# %%



