# %% [markdown]
# # Estrutura condicional - comando if
# 
# #### 1ª forma
# ```
# if (condição):
#     bloco_de_comandos
# ```

# %%
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y:"))
if x < y:
    
    nt("{} é menor que {}.".format(x, y))

# %% [markdown]
# #### 2ª forma
# ```
# if (condição):
#     bloco_de_comandos_1
# else:
#     bloco_de_comandos_2
# ```

# %%
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

if x < y:
    print("{} é menor que {}.".format(x, y))
else:
    print("{} é maior ou igual a {}.".format(x, y))


# %%
x = int(input("Digite o valor de x:1 "))
y = int(input("Digite o valor de y:20 "))

if x < y:
    print("{} é menor que {}.".format(x, y))
else:
    if x == y:
        print("{} é igual a {}.".format(x, y))
    else:
        print("{} é maior que {}.".format(x, y))

# %% [markdown]
# #### 3ª forma
# ```
# if (condição_1):
#     bloco_de_comandos_1
# elif (condição_2):
#     bloco_de_comandos_2
# ...
# elif (condição_n):
#     bloco_de_comandos_n
# ```

# %%
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
if x < y:
    print("{} é menor que {}.".format(x, y))
elif x == y:
    print("{} é igual a {}.".format(x, y))
elif x > y:
    print("{} é maior que {}.".format(x, y))

# %% [markdown]
# #### 4ª forma
# ```
# if (condição_1):
#     bloco_de_comandos_1
# elif (condição_2):
#     bloco_de_comandos_2
# ...
# elif (condição_n):
#     bloco_de_comandos_n
# else:
#     bloco_de_comandos_else
# ```

# %%
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
if x < y:
    print("{} é menor que {}.".format(x, y))
elif x == y:
    print("{} é igual a {}.".format(x, y))
else:
    print("{} é maior que {}.".format(x, y))

# %%



