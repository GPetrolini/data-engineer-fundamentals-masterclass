# %% [markdown]
# # Tipos de dados
# 
# Dados comuns do nosso dia-a-dia podem ser classificados em 4 tipos:
# 
#                              - Inteiros: números sem casa decimal: 10, 5, -4
#                            /
#              - Numéricos - 
#            /               \
#           /                  - Reais: números com casa decima: 3.14, 1075.18, 0.0
# - Dados - 
#           \                      - Lógicos: True ou False
#            \                   /
#              - Não numéricos - 
#                                \
#                                  - Texto (cadeia de caracteres): "Python", "José Maria da Silva", "34567-890"
#                                  
# O Python possui tipos primitivos para cada um desses tipos de dados. São eles o int, float, bool e o str.
# 
# # Operadores aritméticos
# 
# 
# | Operador | Significado   | Exemplo                    |
# |:---|:---|:---|
# |     +    | Adição        | a = 3 + 2                  |
# |     -    | Subtração     | b = 7 - a                  |
# |     *    | Multiplicação | c = a * b                  |
# |     /    | Divisão       | d = 10/3                   |
# |    //    | Quociente     | e = 10//3                  |
# |     %    | Resto         | f = 10%3                   |
# |    **    | Exponenciação | g = 2 ** 3                 |
# |    **    | Radiciação    | h = 16 ** (1/2)            |
# 
# ## Precedência de Operadores
# 
# 1. Parênteses
# 2. Potenciação
# 3. Multiplicação e divisão
# 4. Soma e substração

# %%
# Adição
3 + 2

# %%
# Subtração
7-5

# %%
# Multiplicação

# %%
2 * 3

# %%
3 * 3.5

# %%
4 * 5.0

# %%
# Divisão
9 / 3

# %%
10 / 3

# %%
9 / 3.0

# %%
# Divisão - calculando o coeficiente
5 // 2

# %%
5.0 // 2

# %%
4 // 1.2

# %%
# Divisão - calculando o resto
5 % 2

# %%
9 % 2.5

# %%
# Potenciação: (1) Exponenciação e (2) Radiciação
# (1) Exponenciação
3 ** 2

# %%
2 ** 10

# %%
# (2) Radiciação
# Raiz quadrada de 9
9 ** (1/2)

# %%
# Raiz quadrada de 16 (elevando a 0.5 ao invés da fração 1/2)
16 ** 0.5

# %%
# Raiz cúbica de 27
27 ** (1/3)

# %% [markdown]
# # Exercício de fixação
# 
# Converter as equações em expressões aritméticas válidas no Python. 
# 
# Eq1.
# 
# $ 2+3*4/5-6 $

# %%
2 + 3 * 4 / 5 - 6

# %% [markdown]
# Agora a mesma equação acima, mas alterando a precedência para que as operações de soma e subtração sejam executadas antes das outras. _Dica: use parênteses._

# %%
(2 + 3) * 4 / (5 - 6)

# %% [markdown]
# Eq2. $ \sqrt{\frac{(2-3)^{2}}{4}}$

# %%
((2-3)**2/4)**(1/2)

# %% [markdown]
# # Variáveis e o comando de atribuição
# 
# ## Conceito de variável
# O que é uma [variável](https://pt.wikipedia.org/wiki/Variável_\(programação\) "Conceito de variável no Wikipedia")? De forma bem simples e objetiva, uma **variável** é um espaço na memória (*memória RAM*) do seu computador, utilizada por um programa para armazenar dados. 
# 
# 
# ## Identificadores
# 
# Uma variável precisa necessariamente de um nome, o qual chamamos de **identificador**. Em Python, um identificador é formado apenas por letras (_de A a Z, maiúsculas ou minúsculas, sem acentuação_), dígitos (_0 a 9_) e o _underscore_ ( \_ ). Um identificador deve começar **obrigatoriamente** com uma letra ou *underscore*, e não pode conter espaços, caracteres especiais (@, !, \*, -, &, ˜, etc) ou caracteres acentuados (é, à, ã, ç, í, ö, ü, û, etc..). 
# 
# Portanto, os caracteres permitidos em identificadores são:
# 
# `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789`
# 
# ### Identificadores válidos e inválidos
# Portanto podemos considerar os seguintes identificadores como nomes válidos para variáveis:
# 
# * nome
# * Salario
# * NUMERO10
# * i23ER21
# * \_data\_de\_nascimento\_
# 
# Já os identificadores abaixo não são nomes válidos para variáveis:
# * nome do aluno (*identificadores não podem conter espaços*)
# * Salário (*contém uma letra acentuada*)
# * 10NUMERO (*começa com dígito*)
# * !23ER21 (_possui um caractere especial **!**_)
# * data-de-nascimento (_possui um caractere especial **-**_)
# 
# ### Identificadores significativos e não significativos
# 
# Além de serem válidos, como nos exemplos acima, os **identificadores** precisam ter nomes significativos. Ou seja, ao ver um identificador, o programador deve conseguir perceber que dado está armazenado na variável.
# 
# Os identificadores abaixo, embora sejam válidos, não tem nomes significativos:
# 
# * i23ER1
# * _123
# * BATMAN
# * T
# 
# Embora todos os identificadores acima sejam válidos, não são significativos. Que informação será armazenada nas variáveis _i23ER21_, _\_123_, _BATMAN_ ou _T_? É difícil descobrir.
# 
# Os identificadores abaixo são válidos e tem nomes significativos:
# 
# * salario
# * idade
# * nome
# * nota
# * complementoenderecoparacorrespondencia
# 
# Uma observação importante: para que um nome seja significativo, ele não precisa ser tão longo quanto _complementoenderecoparacorrespondencia_. Por exemplo, o que a variável `dtnasc` armazena? Se você pensou em uma data de nascimento, você acertou. Não precisamos de identificadores longos como *data\_de\_nascimento* para criar identificadores significativos. O ideal é utilizar identificadores mais curtos e fáceis de memorizar e utilizar como _dtnasc_.
# 
# Por fim, uma última informação. Python faz diferenciação entre letras maiúsculas e minúsculas em identificadores. Portanto, os identificadores _nota, Nota e NOTA_ representam três variáveis diferentes.
# 
# ## Criando variáveis
# 
# Variáveis em Python não são **declaradas** como em outras linguagens *(ex: Pascal, C, C++, Java, C#, etc...)* mas **criadas** a partir da atribuição de um valor, uma variável, uma expressão ou um objeto. O comando de atribuição, representado pelo sinal de igualdade (**=**), é o responsável por atribuir (ou armazenar) um valor em uma variável.
# 
# Vejamos agora alguns exemplos:

# %%
idade = 47

# %%
nome = 'José Maria da Silva'

# %%
pi = 3.14159

# %%
aprovado = True

# %% [markdown]
# # Verificando tipos de dados e variáveis
# 
# ## type()
# 
# O Python fornece o método **type()** que retorna o tipo de dados e variáveis. Seu uso é muito simples, basta colocar um objeto, o nome de uma variável ou um valor entre parênteses. 

# %%
type(idade)

# %%
type(2)

# %%
type(nome)

# %%
type('python')

# %%
type(pi)

# %%
type(aprovado)

# %% [markdown]
# ## isinstance()
# 
# Além do método **type()** que retorna o tipo de um objeto, Python fornece o método **isinstance()** que permite verificar se um objeto ou variável (primeiro parâmetro da função) é uma instância de uma classe ou é de um determinado tipo.

# %%
isinstance(5, int)

# %%
isinstance(5, str)

# %%
isinstance(5, float)

# %%
isinstance('Python', str)

# %%
isinstance('Python', int)

# %% [markdown]
# # Imprimindo valores e variáveis
# 
# Python fornece o método print para impressão de valores e variáveis. 
# 
# Algumas células acima, nós criamos as variáveis _nome, idade, pi_ e _aprovado_ e usamos o comando de atribuição para armazenar alguns valores. Que tal imprimir esse valores?

# %%
print('nome')

# %% [markdown]
# Perceba que ao executar o comando *print('nome')*, a palavra **nome** foi impressa.

# %%
print(nome)

# %% [markdown]
# Já nesse exemplo, ao executar o comando *print(nome)*, o resultado apresentado foi o nome `José Maria da Silva`.
# 
# A diferença é que no primeiro exemplo pedimos para o Python imprimir o **texto** `'nome'`, enquanto que no segundo pedimos ao Python para imprimir o conteúdo da variável `nome`. A diferença está no apóstrofo (ou, como alguns costumam chamar, aspas simples). A presença de apóstrofos indica um texto, enquanto que a falta deles indica que se deseja imprimir uma variável.

# %%
print(idade)

# %%
print(pi)

# %%
print(aprovado)

# %% [markdown]
# Quando usamos o método print com uma variável entre parênteses, ele imprime o conteúdo dessa variável, ou seja, o valor que está armazenado dentro dela.
# 
# Nós podemos montar mensagens um pouco mais sofisticadas juntando texto e variáveis em um único comando print(). Para isso, vamos usar o que chamamos de concatenação, ou seja, vamos juntar texto e variáveis com o símbolo +. Veja os exemplos abaixo.

# %%
print('Nome: '+nome)

# %%
# Podemos também usar a vírgula ao invés do símbolo +
print('Nome:',nome)

# %%
# A forma mais utilizada na versão 3 do Python, entretanto, é usar o método format.
print('Meu nome é {} e tenho {} anos'.format(nome, idade))

# %% [markdown]
# # Transformando equações matemáticas em expressões aritméticas
# 
# ### Cálculo da área e perímetro do retângulo
# 
# $area = base \times altura$
# 
# $ perímetro = 2 \times (base + altura)$

# %%
base = 7
altura = 8
area = base * altura
perimetro = 2 * (base + altura)
print(area)

# %% [markdown]
# ### Cálculo da área e comprimento da circunferência
# 
# $ area = \pi \times raio^{2} $
# 
# $ comprimento = 2 \times \pi * raio $

# %%
raio = 2
area = 3.14159 * raio ** 2
comprimento = 2 * 3.14159 * raio
print('Para o raio {}, a área = {} e o comprimento = {}'.format(raio, area, comprimento))

# %% [markdown]
# ### Cálculo da distância euclidiana entre 2 pontos no plano cartesiano
# 
# $ distância = \sqrt{(x_{1}-x_{2})^{2} + (y_{1}-y_{2})^{2}} $

# %%
# Calculando a distância entre os pontos (3,4) e (5,6)
x1 = 3
y1 = 4
x2 = 5
y2 = 6
dist = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
print('A distância entre os pontos({},{}) e ({},{}) = {}.'.format(x1, y1, x2, y2, dist))

# %% [markdown]
# ### Cálculo do delta e das raízes de uma equação do segundo grau
# 
# $ \Delta = b^{2} - 4ac $
# 
# $ x = \frac{-b \pm \sqrt{\Delta}}{2a} $

# %%
# Calculando o Delta e raízes x1 e x2 para a equação y = x^2 - 5x + 6
a = 1
b = -5
c = 6
delta = b**2 - 4*a*c
x1 = (-b+delta**(1/2))/(2*a)
x2 = (-b-delta**(1/2))/(2*a)
print('Delta = {}, x1 = {} e x2 = {}'.format(delta, x1, x2))

# %% [markdown]
# ### Cálculo da área do setor circular (fatia de um círculo)
# 
# $ S = \frac{\alpha \pi r^{2}}{360} $

# %%
# Para um círculo de raio 15, calcular a área de uma fatia com angulo = 45 graus (um pizza)
# Isso equivale a calcular a área de uma das 8 fatias de uma pizza com 30 cm de diâmetro
a = 45
r = 15
s = (a * 3.14159 * r ** 2)/360
print('Num círculo de raio {}cm, o setor circular de ângulo {} terá área = {} cm^2.'.format(r,a,s))

# %%



