# %% [markdown]
# # Comando while
# 
# O while é o comando utilizado para programar repetições no Python baseadas na avaliação de uma condição. Enquanto a condição for verdadeira, o bloco de comandos interno ao while é repetido. Quando a condição se torna falsa, o bloco de comandos deixa de repetir.
# 
# ```python
# while (cond):
#     bloco de comandos
# ```

# %% [markdown]
# Exemplo 1: Digitar os nomes e idades de diversas pessoas, armazenando esses dados em 2 listas.

# %%
lista_idades = []
lista_pessoas = []

nome = input("Digite um nome: ")
while (nome.lower() != 'fim'):
    idade = int(input("Digite uma idade: "))
    lista_idades.append(idade)
    lista_pessoas.append(nome)
    nome = input("Digite um nome: ")
    
print("\n\nNomes digitados\n===============")
print(lista_pessoas)
print("\nIdades\n===============")
print(lista_idades)

# %% [markdown]
# Exemplo 2: Digitar os nomes e idades de 5 pessoas, armazenando esses dados em 2 listas.

# %%
lista_idades = []
lista_pessoas = []
cont = 0

while (cont < 5):
    nome = input("Digite um nome: ")    
    idade = int(input("Digite uma idade: "))
    lista_idades.append(idade)
    lista_pessoas.append(nome)
    cont = cont + 1 # ou cont += 1
    
print("\n\nNomes digitados\n===============")
print(lista_pessoas)
print("\nIdades\n===============")
print(lista_idades)

# %% [markdown]
# Exemplo 3: Calcular a soma dos termos da série, enquanto o valor dos termos for maior que 0.0001
# 
# $S = \frac{1}{1}+\frac{1}{4}+\frac{1}{9}+\frac{1}{16}+...$

# %%
soma = 0 # Acumulador que representa a soma de todos os termos da série
qtde = 0 # Inicialização do contador que conta a quantidade de termos calculados
den = 0 # Inicialização da variável que representa o denominador
termo = 1 # Inicialização do termo = 1 (para conseguir entrar no loop while)
while (termo > 0.0001):
    qtde += 1 # Incrementa a quantidade de termos calculados na série
    den = qtde ** 2 # Calcula o valor do denominador em relação à quantidade
    termo = 1 / den
    soma += termo # Acumula o valor do termo à soma
    print("{}o termo {}/{} = {}".format(qtde, 1, den, termo))    
    
print(soma)

# %%



