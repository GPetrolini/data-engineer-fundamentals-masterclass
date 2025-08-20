# %% [markdown]
# # Funções
# 
# ```python
# def func(lista de parâmetros):
#     """
#     Documentation String
#     """
#     bloco de comandos
#     return # opcional
# ```
#        
# 

# %%
# Exemplo 1
def func_01(a):
    """
    Esse é o documentation string (docstring) da função func_01.
    Essa função simplesmente imprime o valor do argumento passado por parâmetro.
    """
    print(a)

# %%
func_01(5)

# %%
func_01("Python")

# %%
func_01([1, 2, 3, 4])

# %%
# Exemplo 2
def inc(num):
    """
    Exemplo de função com retorno de valor. Essa função recebe um parâmetro, então o incrementa e retorna.
    """
    return num + 1

# %%
a = inc(3)
a

# %%
b = inc(99)
b

# %%
# Exemplo 3
def raiz(r, num):
    """
    Calcula raízes através da operação de potência.
    """
    return num ** (1/r)

# %%
a = raiz(2, 16)
a

# %%
b = raiz(3, 27)
b

# %%
c = raiz(5, 243) # Argumentos posicionais
c

# %%
d = raiz(num = 81, r = 2) # Argumentos nomeados
d

# %%
# Exemplo 3 - parâmetros default
def raiz(num, r = 2):
    """
    Calcula raízes através da operação de potência.
    """
    return num ** (1/r)

# %%
a = raiz(16)
a

# %%
b = raiz(32, 5)
b

# %%
# Exemplo 04
def soma(*nums):
    """
    Exemplo de função usando parâmetros arbitrários
    """
    print(type(nums))
    soma = 0
    for num in nums:
        soma += num
    return soma

# %%
soma(2, 5, 4, 2, 8,7, 1, 0, 2)

# %%



