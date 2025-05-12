# Seções 1.1 a 1.3 do livro-texto

Este Notebook contém apenas alguns exemplos retirados do livro-texto. Use o livro-texto para estudar.

## Seção 1.1 PRIMEIROS PASSOS


```python
x = 10
nome = 'aluno'
nota = 8.75
fez_inscricao = True
```


```python
print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_inscricao))
```

    <class 'int'>
    <class 'str'>
    <class 'float'>
    <class 'bool'>



```python
nome = input("Digite um nome: ")
print(nome)
```

    Digite um nome: Fulano
    Fulano



```python
print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world" % (nome))
```

    Olá Fulano, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world



```python
print("Olá {}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world".format(nome))
```

    Olá Fulano, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world



```python
print(f"Olá {nome}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world")
```

    Olá Fulano, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world


## Operações Matemáticas


```python
operacao_1 = 2 + 3 * 5
operacao_2 = (2 + 3) * 5
operacao_3 = 4 / 2 ** 2
operacao_4 = 13 % 3 + 4
```


```python
print(f"Resultado em operacao_1 = {operacao_1}")
print(f"Resultado em operacao_2 = {operacao_2}")
print(f"Resultado em operacao_3 = {operacao_3}")
print(f"Resultado em operacao_4 = {operacao_4}")
```

    Resultado em operacao_1 = 17
    Resultado em operacao_2 = 25
    Resultado em operacao_3 = 1.0
    Resultado em operacao_4 = 5



```python
a = 2
b = 0.5
c = 1
x = input("Digite o valor de x: ")
y = a * x** 2 + b * x + c
print(f"O resultado de y para x = {x} é {y}.")
```

    Digite o valor de x: 111



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-10-9e18846bddff> in <cell line: 5>()
          3 c = 1
          4 x = input("Digite o valor de x: ")
    ----> 5 y = a * x ** 2 + b * x + c
          6 print(f"O resultado de y para x = {x} é {y}.")


    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'



```python
print(type(a))
print(type(b))
print(type(c))
print(type(x))
```

    <class 'int'>
    <class 'float'>
    <class 'int'>
    <class 'str'>



```python
a = 2
b = 0.5
c = 1
x = input("Digite o valor de x: ")
x = float(x)
y = a * x ** 2 + b * x + c
print(f"O resultado de y para x = {x} é {y}.")
```

    Digite o valor de x: 111
    O resultado de y para x = 111.0 é 24698.5.


## Seção 1.2 ESTRUTURAS LÓGICAS, CONDICIONAIS E DE REPETIÇÃO


```python
a = 5
b = 10
if a < b:
    print("a é menor do que b")
    r = a + b
    print(r)
```

    a é menor do que b
    15



```python
a = 10
b = 5
if a < b:
    print("a é menor do que b")
    r = a + b
    print(r)
else:
    print("a é maior do que b")
    r = a - b
    print(r)
```

    a é maior do que b
    5



```python
codigo_compra = 5111
if codigo_compra == 5222:
    print("Compra à vista.")
elif codigo_compra == 5333:
    print("Compra à prazo no boleto.")
elif codigo_compra == 5444:
    print("Compra à prazo no cartão.")
else:
    print("Código não cadastrado")
```

    Código não cadastrado


### AND, OR, NOT


```python
qtde_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))
if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
```

    Digite a quantidade de faltas: 6
    Digite a média final: 10
    Aluno reprovado!


### Prioridade


```python
A = 15
B = 9
C = 9
print(B == C or A < B and A < C)
print((B == C or A < B) and A < C )
```

    True
    False


### WHILE E FOR


```python
numero = 1
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")
```

    Digite um número: 11
    Número ímpar!
    Digite um número: 0
    Número par!



```python
nome = "Guido"
for c in nome:
    print(c)
```

    G
    u
    i
    d
    o



```python
nome = "Guido"
for i, c in enumerate(nome):
    print(f"Posição = {i}, valor = {c}")
```

    Posição = 0, valor = G
    Posição = 1, valor = u
    Posição = 2, valor = i
    Posição = 3, valor = d
    Posição = 4, valor = o


### CONTROLE DE REPETIÇÃO COM RANGE, BREAK E CONTINUE


```python
for x in range(5):
    print(x)
```

    0
    1
    2
    3
    4



```python
disciplina = "Linguagem de programação"
for c in disciplina:
    if c == 'a':
        break
    else:
        print(c)
```

    L
    i
    n
    g
    u



```python
disciplina = "Linguagem de programação"
for c in disciplina:
    if c == 'a':
        continue
    else:
        print(c)
```

    L
    i
    n
    g
    u
    g
    e
    m
     
    d
    e
     
    p
    r
    o
    g
    r
    m
    ç
    ã
    o


### Procura vogais "a" e "e" em um texto


```python
texto = """
A inserção de comentários no código do programa é uma prática normal.
Em função disso, toda linguagem de programação tem alguma maneira de
permitir que comentários sejam inseridos nos programas.
O objetivo é adicionar descrições em partes do código, seja para documentá-
lo ou para adicionar uma descrição do algoritmo implementado (BANIN, p. 45,
2018)."
"""
for i, c in enumerate(texto):
    if c == 'a' or c == 'e':
        print(f"Vogal '{c}' encontrada, na posição {i}")
    else:
        continue
```

    Vogal 'e' encontrada, na posição 6
    Vogal 'e' encontrada, na posição 13
    Vogal 'e' encontrada, na posição 18
    Vogal 'a' encontrada, na posição 45
    Vogal 'a' encontrada, na posição 47
    Vogal 'a' encontrada, na posição 53
    Vogal 'a' encontrada, na posição 61
    Vogal 'a' encontrada, na posição 67
    Vogal 'a' encontrada, na posição 91
    Vogal 'a' encontrada, na posição 98
    Vogal 'e' encontrada, na posição 100
    Vogal 'e' encontrada, na posição 104
    Vogal 'a' encontrada, na posição 111
    Vogal 'a' encontrada, na posição 113
    Vogal 'e' encontrada, na posição 119
    Vogal 'a' encontrada, na posição 122
    Vogal 'a' encontrada, na posição 127
    Vogal 'a' encontrada, na posição 130
    Vogal 'e' encontrada, na posição 132
    Vogal 'a' encontrada, na posição 135
    Vogal 'e' encontrada, na posição 138
    Vogal 'e' encontrada, na posição 141
    Vogal 'e' encontrada, na posição 151
    Vogal 'e' encontrada, na posição 156
    Vogal 'e' encontrada, na posição 166
    Vogal 'a' encontrada, na posição 168
    Vogal 'e' encontrada, na posição 174
    Vogal 'a' encontrada, na posição 190
    Vogal 'a' encontrada, na posição 192
    Vogal 'e' encontrada, na posição 201
    Vogal 'a' encontrada, na posição 209
    Vogal 'a' encontrada, na posição 216
    Vogal 'e' encontrada, na posição 220
    Vogal 'e' encontrada, na posição 227
    Vogal 'e' encontrada, na posição 230
    Vogal 'a' encontrada, na posição 234
    Vogal 'e' encontrada, na posição 237
    Vogal 'e' encontrada, na posição 252
    Vogal 'a' encontrada, na posição 254
    Vogal 'a' encontrada, na posição 257
    Vogal 'a' encontrada, na posição 259
    Vogal 'e' encontrada, na posição 266
    Vogal 'a' encontrada, na posição 279
    Vogal 'a' encontrada, na posição 281
    Vogal 'a' encontrada, na posição 283
    Vogal 'a' encontrada, na posição 290
    Vogal 'a' encontrada, na posição 295
    Vogal 'e' encontrada, na posição 298
    Vogal 'a' encontrada, na posição 310
    Vogal 'e' encontrada, na posição 324
    Vogal 'e' encontrada, na posição 326
    Vogal 'a' encontrada, na posição 329


## Seção 1.3 Funções


```python
a = 2
b = 1
equacao = input("Digite a fórmula geral da equação linear (a * x + b): ")
print(f"\nA entrada do usuário {equacao} é do tipo {type(equacao)}")
for x in range(5):
    y = eval(equacao)
    print(f"\nResultado da equação para x = {x} é {y}")
```

    Digite a fórmula geral da equação linear (a * x + b): a * x + b
    
    A entrada do usuário a * x + b é do tipo <class 'str'>
    
    Resultado da equação para x = 0 é 1
    
    Resultado da equação para x = 1 é 3
    
    Resultado da equação para x = 2 é 5
    
    Resultado da equação para x = 3 é 7
    
    Resultado da equação para x = 4 é 9



```python
def imprimir_mensagem(disciplina, curso):
    print(f"Minha primeira função em Python desenvolvida na "
          f"disciplina: {disciplina}, do curso: {curso}.")


imprimir_mensagem("Python", "ADS")
```

    Minha primeira função em Python desenvolvida na disciplina: Python, do curso: ADS.



```python
def imprimir_mensagem(disciplina, curso):
    print(f"Minha primeira função em Python desenvolvida na "
          f"disciplina: {disciplina}, do curso: {curso}.")


resultado = imprimir_mensagem("Python", "ADS")
print(f"Resultado = {resultado}")
```

    Minha primeira função em Python desenvolvida nadisciplina: Python, do curso: ADS.
    Resultado = None


### Função que recebe uma data no formato dd/mm/aaaa e converte o mês para extenso


```python
def converter_mes_para_extenso(data):
    mes = '''janeiro fevereiro março
    abril maio junho julho agosto
    setembro outubro novembro
    dezembro'''.split()
    d, m, a = data.split('/')
    mes_extenso = mes[int(m) - 1] # O mês 1, estará na posição 0!
    return f'{d} de {mes_extenso} de {a}'


print(converter_mes_para_extenso('10/05/2021'))
```

    10 de maio de 2021


### FUNÇÕES COM PARÂMETROS DEFINIDOS E INDEFINIDOS


```python
def somar(a, b):
    return a + b

r = somar(2)
print(r)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-35-4456bbb97a27> in <cell line: 4>()
          2     return a + b
          3 
    ----> 4 r = somar(2)
          5 print(r)


    TypeError: somar() missing 1 required positional argument: 'b'



```python
def calcular_desconto(valor, desconto=0):
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto


valor1 = calcular_desconto(100) # Não aplicar nenhum desconto
valor2 = calcular_desconto(100, 0.25) # Aplicar desconto de 25%
print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")
```

    
    Primeiro valor a ser pago = 100
    
    Segundo valor a ser pago = 75.0



```python
def cadastrar_pessoa(nome, idade, cidade):
    print("\nDados a serem cadastrados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")


cadastrar_pessoa("João", 23, "São Paulo")
cadastrar_pessoa("São Paulo", "João", 23)
```

    
    Dados a serem cadastrados:
    Nome: João
    Idade: 23
    Cidade: São Paulo
    
    Dados a serem cadastrados:
    Nome: São Paulo
    Idade: João
    Cidade: 23



```python
def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()

texto = converter_maiuscula(flag_maiuscula=True, texto="João")
print(texto)
```

    JOÃO



```python
def converter_minuscula(texto, flag_minuscula=True):
    if flag_minuscula:
        return texto.lower()
    else:
        return texto.upper()

texto1 = converter_minuscula(flag_minuscula=True, texto="LINGUAGEM de Programação")
texto2 = converter_minuscula(texto="LINGUAGEM de Programação")
print(f"\nTexto 1 = {texto1}")
print(f"\nTexto 2 = {texto2}")
```

    
    Texto 1 = linguagem de programação
    
    Texto 2 = linguagem de programação



```python
def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f"Quantidade de parâmetros = {qtde_parametros}")
    for i, valor in enumerate(args):
        print(f"Posição = {i}, valor = {valor}")


print("\nChamada 1")
imprimir_parametros("São Paulo", 10, 23.78, "João")
print("\nChamada 2")
imprimir_parametros(10, "São Paulo")
```

    
    Chamada 1
    Quantidade de parâmetros = 4
    Posição = 0, valor = São Paulo
    Posição = 1, valor = 10
    Posição = 2, valor = 23.78
    Posição = 3, valor = João
    
    Chamada 2
    Quantidade de parâmetros = 2
    Posição = 0, valor = 10
    Posição = 1, valor = São Paulo


### Parâmetro nominal e não obrigatório


```python
def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
    qtde_parametros = len(kwargs)
    print(f"Quantidade de parâmetros = {qtde_parametros}")
    for chave, valor in kwargs.items():
        print(f"variável = {chave}, valor = {valor}")


print("\nChamada 1")
imprimir_parametros(cidade="São Paulo", idade=33, nome="João")
print("\nChamada 2")
imprimir_parametros(desconto=10, valor=100)
```

    
    Chamada 1
    Tipo de objeto recebido = <class 'dict'>
    
    Quantidade de parâmetros = 3
    variável = cidade, valor = São Paulo
    variável = idade, valor = 33
    variável = nome, valor = João
    
    Chamada 2
    Tipo de objeto recebido = <class 'dict'>
    
    Quantidade de parâmetros = 2
    variável = desconto, valor = 10
    variável = valor, valor = 100


### FUNÇÕES ANÔNIMAS


```python
(lambda x: x + 1)(x=3)
```




    4




```python
(lambda x, y: x + y)(x=3, y=2)
```




    5



### Atribuir a uma variável uma função


```python
somar = lambda x, y: x + y
somar(x=5, y=3)
```




    8




```python
def somar (x, y):
    return x - y

somar(5, 3)
```




    2




```python
somar(3, 5)
```




    -2

<br><sub>Last edited: 2023-08-28 20:31:14</sub>
