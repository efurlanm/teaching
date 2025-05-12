# Classes e métodos

- Atributos: dados
- Métodos: funções
- Encapsulamento: combinar atributos e métodos na mesma entidade, tornar atributos privados
    - Uma classe é um exemplo de encapsulamento
- Herança: reuso do código, herdar atributos e métodos de outra classe
- Polimorfismo: um método definido anteriormente é redefinido com um comportamento diferente


```python
class PrimeiraClasse:

    def imprimir_mensagem(self, nome):
        print(f"Olá {nome}, seja bem vindo!")
        print(self)
```

- "self" é a referência à instância corrente da classe
- usado para referenciar variáveis que pertencem à classe


```python
objeto01 = PrimeiraClasse()
```


```python
PrimeiraClasse
```




    __main__.PrimeiraClasse




```python
objeto01.imprimir_mensagem('João')
```

    Olá João, seja bem vindo!
    <__main__.PrimeiraClasse object at 0x7f27b3ce8e50>



```python

```

"self":


```python
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc() 
```

    Hello my name is John



```python

```


```python
class Calculadora:

    def somar(self, n1, n2):
        return n1 + n2

    def subtrair(self, n1, n2):
        return n1 - n2

    def multiplicar(self, n1, n2):
        return n1 * n2

    def dividir(self, n1, n2):
        return n1 / n2

    def dividir_resto(self, n1, n2):
        return n1 % n2
```

instanciação:


```python
calc = Calculadora()
```

uso da instância:


```python
print('Soma:', calc.somar(4, 3))
```

    Soma: 7



```python
print('Multiplicação:', calc.multiplicar(2, 4))
```

    Multiplicação: 8


---


```python
class Televisao:

    def __init__(self):
        self.volume = 10

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1
```

cria o objeto:


```python
tv = Televisao()
```

valor atual do atributo volume, que foi definido em __init__ :


```python
tv.volume
```




    10




```python
print("Volume ao ligar a tv = ", tv.volume)
```

    Volume ao ligar a tv =  10


chama o método da instância da classe, que aumenta o valor:


```python
tv.aumentar_volume()
```


```python
print("Volume atual = ", tv.volume)
```

    Volume atual =  11


---

## Variáveis e métodos privados

Python possui suporte limitado a este tipo de mecanismo. Usa-se o recurso de "name mangling" (desfiguração de nomes) para "esconder" os nomes. O nome não fica realmente "privado", e na prática pode ser acessado eventualmente.

Para usar mangling coloca-se 2 símbolos de sublinhar no início do nome (e no máx. 1 no final). Python internamente o renomeia acrescentando o nome da classe na frente, tornando-o único.


```python
class ContaCorrente:

    def __init__(self):
        self.__saldo = 123.45

    def depositar(self, valor):
        self.__saldo += valor

    def __imprime(self, valor):
        print(valor)
    
    def consultar_saldo(self):
        self.__imprime(self.__saldo)
```


```python
cc = ContaCorrente()
```

inicialmente dá a impressão de que \_\_saldo\_ é privado:


```python
cc.__saldo
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[104], line 1
    ----> 1 cc.__saldo


    AttributeError: 'ContaCorrente' object has no attribute '__saldo'


porém na verdade ele foi renomeado e ficou "escondido":


```python
cc._ContaCorrente__saldo
```




    123.45



renomear desta forma é também uma técnica para tornar o nome único, evitando overloading de métodos e conflitos de nomes.

com métodos funciona igual, parece que é privado:


```python
cc.__imprime(123.45)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[97], line 1
    ----> 1 cc.__imprime(123.45)


    AttributeError: 'ContaCorrente' object has no attribute '__imprime'


mas na verdade foi apenas renomeado:


```python
cc._ContaCorrente__imprime(123.45)
```

    123.45


## Herança

Permite que uma classe-filha herde os recursos da classe-pai. Em Python, uma classe aceita múltiplas heranças, ou seja, herda recursos de diversas classes. A sintaxe para criar a herança é feita com parênteses após o nome da classe: class NomeClasseFilha(NomeClassePai). Se for uma herança múltipla, cada superclasse deve ser separada por vírgula


```python
class Pessoa:

    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None
```

herança de Pessoa:


```python
class Funcionario(Pessoa):

    def __init__(self):
        self.matricula = 12345
        self.data = '88/88/88'

    def bater_ponto(self):
        # código aqui
        pass

    def fazer_login(self):
        # código aqui
        pass
```


```python
class Cliente(Pessoa):

    def __init__(self):
        self.codigo = None
        self.dataCadastro = None

    def fazer_compra(self):
        # código aqui
        pass

    def pagar_conta(self):
        # código aqui
        pass
```


```python
class FunCli(Funcionario, Pessoa):
    pass
```


```python
fc = FunCli()
```


```python
c = Cliente()
```


```python
fc.nome = "Fulano"
```


```python
fc.data
```




    '88/88/88'




```python
fc.nome
```




    'Fulano'



são instâncias diferentes:


```python
c.nome
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[134], line 1
    ----> 1 c.nome


    AttributeError: 'Cliente' object has no attribute 'nome'



```python
c.nome = 'Ciclano'
print(c.nome, fc.nome)
```

    Ciclano Fulano


## Métodos mágicos

Quando uma classe é criada em Python, ela herda, mesmo que não declarado explicitamente, todos os recursos de uma classe-base chamada object

A funão `dir()` retorna as propriedades e métodos de um objeto. Os nomes que estão com sublinhado são chamados métodos mágicos:


```python
print(dir(FunCli()))
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bater_ponto', 'data', 'fazer_login', 'matricula']


## Método construtor - herança e sobreescrita

função int padrão do Python:


```python
int(12.34)
```




    12



mostrando as propriedades e métodos de int() :


```python
print(dir(int()))
```

    ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']


vamos criar uma classe que herda de int(), vazia, usando `pass`, só para conferir se a herança funciona:


```python
class int45(int):
    pass
```


```python
int45(12.34)
```




    12



vamos criar uma classe que herda int() mas sobrepõe (override) o método de soma para retornar uma constante:


```python
class int888(int):
    def __add__(a, b):
        return 888
```


```python
a = int888(12.34)
a
```




    12




```python
b = int888(34.56)
b
```




    34




```python
a + b
```




    888



Polimorfismo pode usar sobreescrita (override) ou sobrecarga (overload).

Python não suporta sobrecarga de forma direta.


```python
class A :

    def s(self, i=None, j=None) :
        print(type(i))
        if type(i) == int :
            print("Soma:", i + j )
        if type(i) == str :
            print("Ex.: concatenção de string:", i, j)
```


```python
b = A()
```


```python
b.s()
```

    <class 'NoneType'>



```python
b.s(1, 2)
```

    <class 'int'>
    Soma: 3



```python
b.s('1', '2')
```

    <class 'str'>
    Ex.: concatenção de string: 1 2



```python

```

<br><sub>Last edited: 2023-09-17 12:19:08</sub>
