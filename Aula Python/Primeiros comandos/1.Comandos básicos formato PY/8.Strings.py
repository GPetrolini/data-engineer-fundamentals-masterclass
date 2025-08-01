# %% [markdown]
# # Strings
# 
# Em Python, variáveis do tipo `str`, ou **strings**, são as variáveis que armazenam informações de texto (por exemplo: seu nome, seu endereço, o seu tipo sanguíneo, etc). Como em outras linguagens de programação, as strings em Python são uma sequência (ou uma cadeia) de caracteres. Por exemplo, a string `Jupyter Notebook`, cuja representação você pode ver na figura abaixo, é interpretada pelo Python como uma seqüência de caracteres em uma ordem específica. 
# 
# ![Coloque a imagem String.png na mesma pasta que o notebook Strings.ipynb](String.png)
# 
# Ou seja, da mesma forma que em uma lista, cada caractere em uma string possui um índice. Em nosso exemplo, a letra `J` está armazenada no índice 0, a letra `u` no índice 1, e assim por diante. Através da indexação, portanto, podemos acessar uma única posição, ou várias posições. 
# 
# Nessa aula veremos:
# 
# 1. Como criar strings
# 2. Indexação
# 3. Slicing (fatiamento)
# 4. Operadores aplicados a strings
# 5. Imutabilidade das strings
# 6. Métodos do objeto string

# %% [markdown]
# ### 1. Criando strings
# 
# Strings são criadas através de aspas simples (apóstrofos) ou aspas duplas (aspas). 

# %%
'Hello world!!!' # Usando apóstrofos para criar uma string

# %%
"Hello world!!!" # Usando aspas para criar uma string

# %%
"I'm a teacher." # Exemplo de uso de aspas e apóstrofos em um mesmo string

# %%
'Ele é "bonito"... kkk' # Exemplo de uso de aspas e apóstrofos em um mesmo string

# %%
# Criando uma variável string
nome = "Joaquim"

# %%
# Exibindo o conteúdo da variável nome
nome

# %%
# Em outras IDE's, a forma correta de mostrar o conteúdo de uma variável é através do print
print(nome)

# %%
# Verificando o tipo da variável nome
type(nome)

# %%
# Retornando o tamanho do string
len(nome)

# %% [markdown]
# ### 2. Indexação em strings
# 
# Para acessarmos uma posição em particular, vamos utilizar os colchetes. Dentro de colchetes então colocamos o índice que desejamos acessar.
# 
# s\[índice\] => Acessa uma única posição.

# %%
""" 
Definindo a string s = "Python"

+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
  0   1   2   3   4   5
"""
s = "Python"
# Acessando cada caractere armazenado no string s
print(s[0]) # P
print(s[1]) # y
print(s[2]) # t
print(s[3]) # h
print(s[4]) # o
print(s[5]) # n

# %%
""" 
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
 -6  -5  -4  -3  -2  -1
"""
# Acessando cada caractere armazenado no string s (utilizando índices decrescentes)
print(s[-6]) # P
print(s[-5]) # y
print(s[-4]) # t
print(s[-3]) # h
print(s[-2]) # o
print(s[-1]) # n

# %%
# Acessando o caractere armazendo na última posição
# 1a opção
s[5]

# %%
# Acessando o caractere armazendo na última posição
# 2a opção
s[len(s)-1]

# %%
# Acessando o caractere armazendo na última posição
# 3a opção
s[-1]

# %% [markdown]
# ### 3. Slicing (fatiamento) em strings
# 
# Caso você deseje acessar mais de uma posição, você deve utilizar a técnica de *slicing* (ou fatiamento). 
# 
# * `s[ind]` => Acessa uma única posição.
# * `s[inicial:final]` => Acessa os caracteres armazenados entre os índices *ind_inicial* e *ind_inicial-1*
# * `s[inicial:final:inc]` => Acessa os caracteres armazenados entre os índices *inicial* e *ind_inicial-1* com incremento *inc*
# 
# Em nosso exemplo vamos utilizar o string `Jupyter Notebook`.
# 
# ![Coloque a imagem String.png na mesma pasta que o notebook Strings.ipynb](String.png)

# %%
# Redefinindo a string s
s = "Jupyter Notebook"

# %%
# Retornando apenas a palavra Jupyter - 1a opção
s[0:7] # Estamos acessando o string s a partir do índice 0 até o índice 6

# %%
# Retornando apenas a palavra Jupyter - 2a opção
s[-16:-9] # Estamos acessando o string s a partir do índice -16 até o índice -10

# %%
# Retornando apenas a palavra Jupyter - 3a opção
s[:7] # Estamos acessando o string s a partir do início até o índice 6

# %%
# Retornando apenas a palavra Jupyter - 4a opção
s[:-9] # Estamos acessando o string s a partir do início até o índice -10

# %%
# Retornando apenas a palavra Notebook - 1a opção
s[8:16] # Estamos acessando o string s a partir do índice 8 até o índice 15

# %%
# Retornando apenas a palavra Notebook - 2a opção
s[-8:] # Estamos acessando o string s a partir do índice -16 até o índice -9

# %%
# Retornando apenas a palavra Notebook - 3a opção
s[8:] # Estamos acessando o string s a partir do início até o índice 6

# %%
# Nós podemos acessar posições não contínuas
s[0:7:2] # Serão acessados os caracteres armazenados nas posiçõs 0, 2, 4 e 6 (o incremento informado foi 2)

# %%
# Serão acessadas os caracteres armazenados desde o início até o final, com incremento de 3 (posições 0,3,6,9,12,15)
s[::3] 

# %%
# Com incrementos negativos, podemos acessar o string em ordem invertida - 1a opçao
s[-1::-1] # da posição -1 até o início, com incremento -1

# %%
# Com incrementos negativos, podemos acessar o string em ordem invertida - 2a opçao
s[-1:-17:-1] # da posição -1 até a posição -16, com incremento -1

# %%
# Com incrementos negativos, podemos acessar o string em ordem invertida - 3a opçao
s[16::-1] # da posição 16 até p início, com incremento -1

# %%
# Com incrementos negativos, podemos acessar o string em ordem invertida - 4a opçao
s[::-1] # do final até o início, com incremento -1

# %%
# Acessando partes do string, a partir do início
p = "Python"
print(p[:0]) # ''
print(p[:1]) # 'P'
print(p[:2]) # 'Py'
print(p[:3]) # 'Pyt'
print(p[:4]) # 'Pyth'
print(p[:5]) # 'Pytho'
print(p[:6]) # 'Python'
print(p[:])  # 'Python'

# %%
print(p[0:1]) # 'P'
print(p[0:2]) # 'Py'
print(p[0:3]) # 'Pyt'
print(p[0:4]) # 'Pyth'
print(p[0:5]) # 'Pytho'
print(p[0:6]) # 'Python'
print(p[0:])  # 'Python'

# %%
# Acessando partes do string, de uma posição qualquer até o final
print(p[:])  # 'Python'
print(p[0:]) # 'Python'
print(p[1:]) # 'ython'
print(p[2:]) # 'thon'
print(p[3:]) # 'hon'
print(p[4:]) # 'on'
print(p[5:]) # 'n'
print(p[6:]) # ''

# %% [markdown]
# ### 4. Operadores aplicados a strings
# 
# | Operador | Significado   | Exemplo                    |
# |:---|:---|:---|
# | s\[ind\] | Acesso a uma posição | `s[0]` |
# | s\[i:f\] | Acesso a uma faixa de posições | `s[1:3]` |
# | s\[i:f:inc\] | Acesso a uma faixa de posições com incremento | `s[0:15:3]` |
# | s1 + s2 | Concatenação de strings | `novastr = s1 + s2` |
# | s\*n | Retorna um string contendo n repetições de s | `s = 'ABC'*10` |
# | s1 in s2 | Retorna True se o substring *s1* está contido em *s2* | `'ABC' in 'ABCDEFGH'` |
# | s1 not in s2 | Retorna True se o substring *s1* não está contido em *s2* | `'XYZ' not in 'ABCDEFGH'` |

# %%
s = "A linguagem Python é demais!"
s1 = "Python"
print(s[0])  # "A"
print(s[2:11]) # "linguagem"
print(s[::-1]) # ""!siamed é nohtyP megaugnil A"
s2 = s + " Sensacional!!!" # Concatenação
print(s2)
s3 = s1*3 # Concatenando o string s1 3 vezes
print(s3)
print("O substring '{}' está contindo em '{}' => {}".format(s1, s, s1 in s))
print("O substring '{}' não está contindo em '{}' => {}".format(s3, s2, s3 not in s2))

# %% [markdown]
# ### 5. Strings são imutáveis
# 
# Vamos supor que queremos trocar um único caractere digitado errado em um string.

# %%
s = "PythoM" # Python digitado com erro
s[5] = "n" # tentando corrigir, substituindo o caractere M armazenado no índice pelo n

# %%
# Para corrigir vamos precisar redefinir o string
s = "Python"
s

# %% [markdown]
# ### 6. Métodos do objeto String
# 
# | Método | Descrição | Exemplo |
# |:------------|:---------------------------------------------------------------------------------------------|:--------------|
# | [capitalize()](https://www.programiz.com/python-programming/methods/string/capitalize) | Retorna uma cópia da string com primeiro caractere maiúsculo e os caracteres restantes em minúsculo | `s.capitalize()`|
# | [casefold()](https://www.programiz.com/python-programming/methods/string/casefold) | Retorna uma cópia da string convertido para letras minúsculas | `s.casefold()` |
# | [center()](https://www.programiz.com/python-programming/methods/string/center) | Retorna uma cópia da string centralizada e preenchida com o caractere especificado (*default* = espaço em branco) | `s.center(20)` |
# | [center()](https://www.programiz.com/python-programming/methods/string/center) | Retorna uma cópia da string centralizada e preenchida com o caractere especificado (*default* = espaço em branco) | `s.center(20, '*')` |
# | [count()](https://www.programiz.com/python-programming/methods/string/count) | Retorna o número de ocorrências de um determinado substring | `s.count('abc')` |
# | [encode()](https://www.programiz.com/python-programming/methods/string/encode) | Retorna uma cópia da string utilizando um determinando *encoding* (*default* = UTF-8)| `s.encode()`|
# | [endswith()](https://www.programiz.com/python-programming/methods/string/endswith) | Retorna `True` se uma string terminar com o sufixo especificado | `s.endswith("python")` |
# | [expandtabs()](https://www.programiz.com/python-programming/methods/string/expandtabs) | Retorna uma cópia da string no qual os caracteres de tabulação `\t` são substituídos por caracteres de espaço em branco | s.expandtabs(3)
# | [find()](https://www.programiz.com/python-programming/methods/string/find) | Retorna o índice da primeira ocorrência da substring. Se não encontrado, retorna -1 | `s.find('python')` |
# | [format()](https://www.programiz.com/python-programming/methods/string/format) | Formata a string de entrada em uma string de saída | `"{} é {}".format("Python", "demais!")` |
# | [index()](https://www.programiz.com/python-programming/methods/string/index) | Retorna o índice da primeira ocorrência de uma substring dentro da string. Se a substring não for encontrada, levanta uma exceção | `s.index('python')`|
# | [isalnum()](https://www.programiz.com/python-programming/methods/string/isalnum) | Retorna `True` se todos os caracteres na string forem alfanuméricos (letras ou números) | `s.isalnum()`|
# | [isalpha()](https://www.programiz.com/python-programming/methods/string/isalpha) | Retorna `True` se a string tiver apenas letras |`s.isalpha()`|
# | isascii() | Retorna True se todos os caracteres na string forem ASCII | `s.isascii()`|
# | [isdecimal()](https://www.programiz.com/python-programming/methods/string/isdecimal) | Retorna `True` se todos os caracteres na string forem decimais (0 a 9) | `s.isdecimal()` |
# | [isdigit()](https://www.programiz.com/python-programming/methods/string/isdigit) | Retorna `True` se todos os caracteres na string forem dígitos (ex: 3²) | `s.isdigit()`|
# | [isidentifier()](https://www.programiz.com/python-programming/methods/string/isidentifier) | Retorna `True` se a string for um identificador válido em Python | `s.isidentifier()`|
# | [islower()](https://www.programiz.com/python-programming/methods/string/islower) | Retorna `True` se todos as letras da string forem letras minúsculas | `s.islower()` |
# | [isnumeric()](https://www.programiz.com/python-programming/methods/string/isnumeric) | Retorna `True` se todos os caracteres na string forem numéricos (ex: ½) | `s.isnumeric()`|
# | [isprintable()](https://www.programiz.com/python-programming/methods/string/isprintable) | Retorna `True` se todos os caracteres da string podem ser impressos | `s.isprintable()`|
# | [isspace()](https://www.programiz.com/python-programming/methods/string/isspace) | Retorna `True` se houverem apenas espaços em branco na string | `s.isspace()` |
# | [istitle()](https://www.programiz.com/python-programming/methods/string/istitle) | Retorna `True` se a string estiver em formato de *título*, ou seja, se cada palavra da string começa com letra maiúscula e tem o restante das letras minúsculas | `s.istitle()`|
# | [isupper()](https://www.programiz.com/python-programming/methods/string/isupper) | Retorna `True` se todos as letras do string forem letras maiúsculas | `s.isupper()` |
# | [ljust()](https://www.programiz.com/python-programming/methods/string/ljust) | Retorna uma cópia da string justificada à esquerda| `s.ljust(20)`|
# | [lower()](https://www.programiz.com/python-programming/methods/string/lower) | Retorna uma cópia da string com as letras maiúsculas convertidas em minúsculas | `s.lower()`|
# | [lstrip()](https://www.programiz.com/python-programming/methods/string/lstrip) | Retorna uma cópia da string com os caracteres passados por parâmetro removidos do início da string | `s.lstrip(' *@')` |
# | [partition()](https://www.programiz.com/python-programming/methods/string/partition) | Divide a string e retorna uma tupla contendo a parte antes do separador (primeira ocorrência), a string de argumento (separador) e a parte após o separador | `s.partition('@')`|
# | [replace()](https://www.programiz.com/python-programming/methods/string/replace) | Retorna uma cópia da string onde todas as ocorrências de uma substring são substituídas por outra | `s.partition('@',' at ')`|
# | [rfind()](https://www.programiz.com/python-programming/methods/string/rfind) | Retorna o índice da última ocorrência da substring. Se não encontrado, retorna -1 | `s.rfind('python')` |
# | [rindex()](https://www.programiz.com/python-programming/methods/string/rindex) | Retorna o índice da última ocorrência da substring dentro da string. Se a substring não for encontrada, levanta uma exceção | `s.rindex('python')`|
# | [rjust()](https://www.programiz.com/python-programming/methods/string/rjust) | Retorna uma cópia da string justificada à direita | `s.rjust(20)`|
# | [rpartition()](https://www.programiz.com/python-programming/methods/string/partition) | Divide a string e retorna uma tupla contendo a parte antes do separador (última ocorrência), a string de argumento (separador) e a parte após o separador | `s.rpartition('@')`|
# | [rsplit()](https://www.programiz.com/python-programming/methods/string/rsplit) | Divide a string à partir da direita (última posição), usando um separador passado por parâmetro, e retorna uma lista de strings| `s.rsplit(';')`|
# | [rstrip()](https://www.programiz.com/python-programming/methods/string/rstrip) | Retorna uma cópia da string com os caracteres passados por parâmetro removidos do final da string | `s.rstrip('!?.')` |
# | [split()](https://www.programiz.com/python-programming/methods/string/split) | Divide a string à partir da esquerda (primeira posição), usando um separador passado por parâmetro, e retorna uma lista de strings| `s.split(';')`|
# | [splitlines()](https://www.programiz.com/python-programming/methods/string/splitlines) | Divide e retorna as linhas contidas em uma string  | `s.splitlines()`|
# | [starstwith()](https://www.programiz.com/python-programming/methods/string/startswith) | Retorna `True` se uma string começar com o prefixo especificado | `s.starstwith("Python")` |
# | [strip()](https://www.programiz.com/python-programming/methods/string/strip) | Retorna uma cópia da string com os caracteres passados por parâmetro removidos do início e do final da string | `s.strip(' *@')` |
# | [swapcase()](https://www.w3schools.com/python/ref_string_swapcase.asp) | Retorna uma cópia da string com letras minúsculas convertidas em maiúsculas e vice-versa | `s.swapcase()`|
# | [title()](https://www.programiz.com/python-programming/methods/string/title) | Retorna uma cópia da string com a primeira letra de cada palavra convertida para maiúscula | `s.title()` |
# | [upper()](https://www.programiz.com/python-programming/methods/string/upper) | Retorna uma cópia da string com as letras minúsculas convertidas em maiúsculas | `s.upper()`|
# | [zfill()](https://www.programiz.com/python-programming/methods/string/zfill) | Retorna uma cópia da string preenchida com 0s (zeros) à esquerda | `s.zfill(8)`|

# %% [markdown]
# ### Exemplo do método capitalize()

# %%
s = "a linguagem python é demais!"
s.capitalize()

# %%
# Importante ressaltar que a string s não foi alterada
s

# %%
s1 = s.capitalize()
print(s)
print(s1)

# %% [markdown]
# ### Exemplo dos métodos casefold(),  lower() e upper()

# %%
s = "AbCdEf"
s1 = s.casefold()
s1

# %%
s2 = s.lower()
s2

# %%
s3 = s.upper()
s3

# %%
# casefold() é mais agressivo em sua conversão se comparado ao lower()
s4 = "Der Fluß"
s5 = s4.casefold()
s5

# %%
s6 = s4.lower()
s6

# %% [markdown]
# ### Exemplo do método center()

# %%
s = "PYTHON"
s

# %%
s1 = s.center(20) # Centralizar s em um string de tamanho 20 - completa com espaços a esquerda e direita
s1

# %%
s2 = s.center(30, "*") # Centralizar s em um string de tamanho 30 - completa com espaços a esquerda e direita
s2

# %% [markdown]
# ### Exemplo do método count()

# %%
s = "A linguagem Python é demais!"
s.count("a")

# %%
s.count("A")

# %%
s.count("b")

# %%
s.count("demais")

# %% [markdown]
# ### Exemplo do método encode()

# %%
s = "Mоето име е Päivi"
s1 = s.encode() # Codifica usando o UTF-8 por padrão
s1

# %% [markdown]
# ### Exemplo dos métodos endswith() e startswith()

# %%
s = "A linguagem Python é demais!"
s.endswith("demais") # False

# %%
s.endswith("demais!") # True

# %%
s.endswith("demais!", 12) # True - Verifica se o substring a partir da posição 12 terminar com "demais!"

# %%
s[2:18] # Substring formado da posição 2 à 17

# %%
s.endswith("Python", 2, 18) # True

# %%
s.startswith("A l") # True

# %%
s.startswith("Python") # False

# %%
s.startswith("Python", 12) # True

# %% [markdown]
# ### Exemplo do método expandtabs()

# %%
s = "col1\tcol2\tcol3"
print(s)

# %%
s1 = s.expandtabs() # Substitui as tabulações por espaços (default = 8)
print(s1)

# %%
print("Tabsize =  5",s.expandtabs(5))
print("Tabsize =  6",s.expandtabs(6))
print("Tabsize =  7",s.expandtabs(7))
print("Tabsize =  8",s.expandtabs())
print("Tabsize =  9",s.expandtabs(9))
print("Tabsize = 10",s.expandtabs(10))

# %% [markdown]
# ### Exemplo dos métodos find(), rfind(), index() e rindex()

# %%
s = "A linguagem Python é demais! Python é sensacional."
s.find("Python") # Procura pelo substring "Python" no string s usando o método find()

# %%
s.rfind("Python") # Procura pelo substring "Python" no string s usando o método rfind()

# %%
s.index("Python") # Procura pelo substring "Python" no string s usando o método index()

# %%
s.rindex("Python") # Procura pelo substring "Python" no string s usando o método rindex()

# %%
s.find("python") # Procura pelo substring "python" no string s usando o método find()

# %%
s.rfind("python") # Procura pelo substring "python" no string s usando o método rfind()

# %%
s.index("python") # Procura pelo substring "python" no string s usando o método index()

# %%
s.rindex("python") # Procura pelo substring "python" no string s usando o método rindex()

# %%
s1 = "Olá! Este é um exemplo. Este é outro exemplo."
s1.find("Este") # Procura pelo substring "Este" no string s usando o método find()

# %%
s1.rfind("Este") # Procura pelo substring "Este" no string s usando o método rfind()

# %%
s1.index("Este") # Procura pelo substring "Este" no string s usando o método index()

# %%
s1.rindex("Este") # Procura pelo substring "Este" no string s usando o método rindex()

# %%
s1.find("Este", 15) # Procura pelo substring "Este" no string s, a partir do índice 15 usando o método find()

# %%
s1.index("Este", 15) # Procura pelo substring "Este" no string s, a partir do índice 15 usando o método index()

# %%
s1.find("Este", 10, 20) # Procura pelo substring "Este" no string s, entre os índices 10 e 19 usando o método find()

# %%
s1.index("Este", 10, 20) # Procura pelo substring "Este" no string s, entre os índices 10 e 19 usando o método index()

# %% [markdown]
# ### Exemplo do método format()

# %%
nome = "Joaquim"
idade = 60
print("Meu nome é {} e tenho {} anos.".format(nome, idade))

# %%
print("Meu nome é {0} e tenho {1} anos.".format(nome, idade))

# %%
print("Meu nome é {} e tenho {} anos.\nRepetindo... Meu nome é {} e tenho {} anos.".format(nome, idade, nome, idade))

# %%
print("Meu nome é {0} e tenho {1} anos.\nRepetindo... Eu tenho {1} anos e meu nome é {0}.".format(nome, idade))

# %%
print("Meu nome é {name} e tenho {age} anos.".format(age=18, name="Pedro"))

# %% [markdown]
# ### Exemplo do método isalnum()

# %%
s = "D3C1FR4NDO"
s.isalnum() 

# %%
s1 = "D3C1FR4NDO 0 CÓD1G0" 
s1.isalnum() # Falso por causa da presença de espaços

# %% [markdown]
# ### Exemplo do método isalpha()

# %%
s = "D3C1FR4NDO"
s.isalpha()

# %%
s1 = "CÓDIGO"
s1.isalpha()

# %%
s2 = "DECIFRANDO O CODIGO"
s2.isalpha()

# %% [markdown]
# ### Exemplo do método isascii()

# %%
cidade = 'ӓmsterdӓm'
cidade.isascii()

# %%
cidade = 'amsterdam'
cidade.isascii()

# %% [markdown]
# A tabela [ASCII](https://pt.wikipedia.org/wiki/ASCII) é composta por 128 "caracteres" (sendo a maioria caracteres "imprimíveis") e não contempla caracteres acentuados.

# %% [markdown]
# ### Exemplo dos métodos isdecimal(), isdigit() e isnumeric()
# 
# * isdecimal() => 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# * isdigit()   => caracteres decimais + subscrito e sobrescrito
# * isnumeric   => caracteres decimais + subscrito e sobrescrito + caracteres UNICODE que representem frações, números romanos, etc

# %%
a = "12345"
b = "1234²"
c = "123²½"
print("a.isdecimal() = ", a.isdecimal())
print("b.isdecimal() = ", b.isdecimal())
print("c.isdecimal() = ", c.isdecimal())
print("="*25)
print("a.isdigit() = ", a.isdigit())
print("b.isdigit() = ", b.isdigit())
print("c.isdigit() = ", c.isdigit())
print("="*25)
print("a.isnumeric() = ", a.isnumeric())
print("b.isnumeric() = ", b.isnumeric())
print("c.isnumeric() = ", c.isnumeric())

# %% [markdown]
# ### Exemplo do método isidentifier()

# %%
s = "i23ER21"
s.isidentifier()

# %%
s = "_i23ER21"
s.isidentifier()

# %%
s = "nome-aluno"
s.isidentifier()

# %%
s = "nome aluno"
s.isidentifier()

# %%
s = "nome_aluno"
s.isidentifier()

# %% [markdown]
# ### Exemplo dos métodos islower() e isupper()

# %%
s = "nome_aluno"
s.islower()

# %%
s.isupper()

# %%
s1 = "nomeAluno"
s1.islower()

# %%
s1.isupper()

# %%
s2 = "minha senh@ é 1234"
s2.islower()

# %%
s2.isupper()

# %%
s3 = "TUDO MAIÚSCULO!!!"
s3.islower()

# %%
s3.isupper()

# %% [markdown]
# ### Exemplo do método isprintable()

# %%
s = "col1\tcol2"
s.isprintable()

# %%
s1 = s.expandtabs()
s1.isprintable()

# %%
s2 = "linha1\nlinha2"
s2.isprintable()

# %% [markdown]
# ### Exemplo do método isspace()

# %%
s1 = "A B"
s1[0].isspace()

# %%
s1[1].isspace()

# %%
s1[2].isspace()

# %% [markdown]
# ### Exemplo do método istitle()

# %%
titulo = "A Linguagem Python"
titulo.istitle()

# %%
titulo = "A Linguagem de Programação Python" # de => False
titulo.istitle()

# %%
titulo = "A Linguagem DE Programação Python" # DE => False
titulo.istitle()

# %%
titulo = "A Linguagem De Programação Python"
titulo.istitle()

# %% [markdown]
# ### Exemplo dos métodos ljust() e rjust()

# %%
s = "Esquerda".ljust(20)
s

# %%
s1 = "Direita".rjust(20)
s1

# %%
s2 = "Esquerda".ljust(20,"<")
s2

# %%
s3 = "Direita".rjust(20,">")
s3

# %% [markdown]
# ### Exemplo dos métodos lstrip(), rstrip() e strip()

# %%
s = "      ABC   "
s1 = s.lstrip()
s1

# %%
s2 = s.rstrip()
s2

# %%
s3 = s.strip()
s3

# %%
link = "https://www.python.org/"
s4 = link.lstrip("hpst:/")
s4

# %%
s5 = link.rstrip("hpst:/")
s5

# %%
s6 = link.strip("hpst:/")
s6

# %% [markdown]
# ### Exemplo dos métodos partition(), rpartition(), split() e rsplit()

# %%
email = "pessoa@dominio.com.br"

# %%
t1 = email.partition("@")
t1

# %%
type(t1)

# %%
l1 = email.split("@")
l1

# %%
type(l1)

# %%
l2 = email.rsplit("@")
l2

# %%
t2 = email.partition(".")
t2

# %%
l3 = email.split(".")
l3

# %%
l4 = email.rsplit(".")
l4

# %%
l5 = email.split(".", 1)
l5

# %%
l6 = email.rsplit(".", 1)
l6

# %%
seq = "012.345.678.910"
t3 = seq.partition(".")
t3

# %%
t4 = seq.rpartition(".")
t4

# %%
print(seq.split("."))
print(seq.split(".", 1))
print(seq.split(".", 2))
print(seq.split(".", 3))

# %%
print(seq.rsplit("."))
print(seq.rsplit(".", 1))
print(seq.rsplit(".", 2))
print(seq.rsplit(".", 3))

# %% [markdown]
# ### Exemplo do método replace()

# %%
msg = "Minha biblioteca favorita é numpy."
print(msg)
msg2 = msg.replace("numpy", "pandas")
print(msg2)

# %%
msg3 = "Eu gosto de cães. Os cães são muito legais. Os cães são companheiros."
print(msg3)
msg4 = msg3.replace("cães", "labradores", 2)
print(msg4)

# %% [markdown]
# ### Exemplo do método splitlines()

# %%
s = "Essa é\numa\nstring\n\ncom várias\nlinhas"
print(s)

# %%
linhas = s.splitlines()

# %%
linhas

# %%
type(linhas)

# %% [markdown]
# ### Exemplo do método swapcase()

# %%
s = "MAIÚSCULO | minúsculo!"
s1 = s.swapcase()
print(s)
print(s1)

# %% [markdown]
# ### Exemplo do método title()

# %%
titulo = "a linguagEm de programação pyThon"
novo_titulo = titulo.title()
print(novo_titulo)

# %% [markdown]
# ### Exemplo do método zfill()

# %%
cod_prod1 = "123".zfill(6)
cod_prod1

# %%
cod_prod2 = "234".zfill(8)
cod_prod2

# %%
cod_prod3 = "123456".zfill(5)
cod_prod3

# %%



