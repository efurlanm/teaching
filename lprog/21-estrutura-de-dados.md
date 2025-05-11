# Seção 2.1 - Estruturas de Dados

Este Notebook contém alguns exemplos retirados do livro-texto.

### Sequências


```python
texto = "Aprendendo Python na disciplina de linguagem de programação."
print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")
```

    Tamanho do texto = 60
    Python in texto = True
    Quantidade de y no texto = 1
    As 5 primeiras letras são: Aprend



```python
texto = "Aprendendo Python na disciplina de linguagem de programação."
print(texto.upper())
print(texto.replace("i", 'XX'))
```

    APRENDENDO PYTHON NA DISCIPLINA DE LINGUAGEM DE PROGRAMAÇÃO.
    Aprendendo Python na dXXscXXplXXna de lXXnguagem de programação.


### Listas


```python
vogais = ['a', 'e', 'i', 'o', 'u']
for vogal in vogais:
    print(f'Posição = {vogais.index(vogal)}, valor = {vogal}')
```

    Posição = 0, valor = a
    Posição = 1, valor = e
    Posição = 2, valor = i
    Posição = 3, valor = o
    Posição = 4, valor = u



```python
vogais = []
print(f"Tipo do objeto vogais = {type(vogais)}")
vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')
for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")
```

    Tipo do objeto vogais = <class 'list'>
    Posição = 0, valor = a
    Posição = 1, valor = e
    Posição = 2, valor = i
    Posição = 3, valor = o
    Posição = 4, valor = u



```python
frutas = ["maça", "banana", "uva", "mamão", "maça"]
notas = [8.7, 5.2, 10, 3.5]
print("maça" in frutas)  # True
print("abacate" in frutas)  # False
print("abacate" not in frutas)  # True
print(min(frutas))  # banana
print(max(notas))  # 10
print(frutas.count("maça"))  # 2
print(frutas + notas)
print(2 * frutas)
```

    True
    False
    True
    banana
    10
    2
    ['maça', 'banana', 'uva', 'mamão', 'maça', 8.7, 5.2, 10, 3.5]
    ['maça', 'banana', 'uva', 'mamão', 'maça', 'maça', 'banana', 'uva', 'mamão', 'maça']



```python
lista = ['Python', 30.61, "Java", 51, ['a', 'b', 20], "maça"]
print(f"Tamanho da lista = {len(lista)}")
for i, item in enumerate(lista):
    print(f"Posição = {i}, valor = {item} --> tipo"
          f" individual = {type(item)}")
print("\nExemplos de slices:\n")
print("lista[1] = ", lista[1])
print("lista[0:2] = ", lista[0:2])
print("lista[:2] = ", lista[:2])
print("lista[3:5] = ", lista[3:5])
print("lista[3:6] = ", lista[3:6])
print("lista[3:] = ", lista[3:])
print("lista[-2] = ", lista[-2])
print("lista[-1] = ", lista[-1])
print("lista[4][1] = ", lista[4][1])
```

    Tamanho da lista = 6
    Posição = 0, valor = Python --> tipo individual = <class 'str'>
    Posição = 1, valor = 30.61 --> tipo individual = <class 'float'>
    Posição = 2, valor = Java --> tipo individual = <class 'str'>
    Posição = 3, valor = 51 --> tipo individual = <class 'int'>
    Posição = 4, valor = ['a', 'b', 20] --> tipo individual = <class 'list'>
    Posição = 5, valor = maça --> tipo individual = <class 'str'>
    
    Exemplos de slices:
    
    lista[1] =  30.61
    lista[0:2] =  ['Python', 30.61]
    lista[:2] =  ['Python', 30.61]
    lista[3:5] =  [51, ['a', 'b', 20]]
    lista[3:6] =  [51, ['a', 'b', 20], 'maça']
    lista[3:] =  [51, ['a', 'b', 20], 'maça']
    lista[-2] =  ['a', 'b', 20]
    lista[-1] =  maça
    lista[4][1] =  b


### map()


```python
linguagens = 'Python Java JavaScript C C# C++ Swift Go Kotlin'.split()
```


```python
linguagens
```




    ['Python', 'Java', 'JavaScript', 'C', 'C#', 'C++', 'Swift', 'Go', 'Kotlin']




```python
nova_lista = map(lambda x: x.lower(), linguagens)
```


```python
nova_lista
```




    <map at 0x7d4397086b30>




```python
list(nova_lista)
```




    ['python', 'java', 'javascript', 'c', 'c#', 'c++', 'swift', 'go', 'kotlin']



Outro exemplo


```python
def evaluate(x):
    print(x)

mymap = map(evaluate, [1,2,3]) # não imprime nada ainda
print(mymap)

```

    <map object at 0x7d4397086080>


next() retorna o próximo item de um iterador


```python
next(mymap)
```

    1



```python

next(mymap)
next(mymap)
next(mymap)
```

    2
    3



    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-30-4bd46ba7f6f8> in <cell line: 3>()
          1 next(mymap)
          2 next(mymap)
    ----> 3 next(mymap)
    

    StopIteration: 


### filter()


```python
num = list(range(21))
```


```python
num
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]




```python
a = filter(lambda x: x % 2 == 0, num)
a
```




    <filter at 0x7d4364532110>




```python
list(a)
```




    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



## Tuplas

- Tuplas são imutáveis


```python
tupla01 = ()  # tupla vazia
tupla01
```




    ()




```python
tupla01 = (1, 2, 3)
tupla01
```




    (1, 2, 3)




```python
vogais = ('a', 'e', 'i', 'o', 'u')
```

enumerate() : qdo precisamos de um contador e um valor


```python
 for p, x in enumerate(vogais) :
    print(p, x)
```

    0 a
    1 e
    2 i
    3 o
    4 u


## Set

- Armazena vários itens em uma única variável
- Não permite itens duplicados, não é ordenado, não é indexado, não pode ser alterado (porém pode ser eliminado ou adicionado)


```python
 set1 = {'a', 'b', 'c'}
 set1
```




    {'a', 'b', 'c'}




```python
set1.add('a')
set1
```




    {'a', 'b', 'c'}




```python
set1 = set(['a', 'b', 'c'])
```


```python
set1
```




    {'a', 'b', 'c'}



### Dicionário

- Pode ser alterado, não pode duplicado.


```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```


```python
thisdict
```




    {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}




```python
thisdict['model']
```




    'Mustang'



### Array NumPy

- NumPy é uma bilbioteca para computação científica, bastante utilizada.


```python
import numpy as np

matriz = np.array([[1, 2], [3, 4]])
```


```python
matriz
```




    array([[1, 2],
           [3, 4]])




```python
np.zeros((3, 3))
```




    array([[0., 0., 0.],
           [0., 0., 0.],
           [0., 0., 0.]])




```python
np.ones((2,2))
```




    array([[1., 1.],
           [1., 1.]])




```python
np.eye(4)    # matriz identidade
```




    array([[1., 0., 0., 0.],
           [0., 1., 0., 0.],
           [0., 0., 1., 0.],
           [0., 0., 0., 1.]])




```python
np.eye(4).sum()  # também: min, máx, mean
```




    4.0




```python
np.ones((1,5))
```




    array([[1., 1., 1., 1., 1.]])




```python
numpy.ones((1,5)).reshape(5,1)
```




    array([[1.],
           [1.],
           [1.],
           [1.],
           [1.]])





<hr color='green' size=10>

### Biblioteca Pandas (introdução)


```python
import pandas as pd
```


```python
mydataset = {
  'carros': ["BMW", "Volvo", "Ford"],
  'passageiros': [3, 7, 2]
}
```


```python
mydataset
```




    {'carros': ['BMW', 'Volvo', 'Ford'], 'passageiros': [3, 7, 2]}




```python
myvar = pd.DataFrame(mydataset)
```


```python
myvar
```





  <div id="df-e14ba11e-9f44-4422-ba8f-7d6accd1d620" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>carros</th>
      <th>passageiros</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BMW</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Volvo</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ford</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-e14ba11e-9f44-4422-ba8f-7d6accd1d620')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-e14ba11e-9f44-4422-ba8f-7d6accd1d620 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-e14ba11e-9f44-4422-ba8f-7d6accd1d620');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


<div id="df-962ab4fd-0ee1-477e-b1fa-4d49ed52d8ad">
  <button class="colab-df-quickchart" onclick="quickchart('df-962ab4fd-0ee1-477e-b1fa-4d49ed52d8ad')"
            title="Suggest charts."
            style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
  </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

  <script>
    async function quickchart(key) {
      const quickchartButtonEl =
        document.querySelector('#' + key + ' button');
      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
      quickchartButtonEl.classList.add('colab-df-spinner');
      try {
        const charts = await google.colab.kernel.invokeFunction(
            'suggestCharts', [key], {});
      } catch (error) {
        console.error('Error during call to suggestCharts:', error);
      }
      quickchartButtonEl.classList.remove('colab-df-spinner');
      quickchartButtonEl.classList.add('colab-df-quickchart-complete');
    }
    (() => {
      let quickchartButtonEl =
        document.querySelector('#df-962ab4fd-0ee1-477e-b1fa-4d49ed52d8ad button');
      quickchartButtonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';
    })();
  </script>
</div>
    </div>
  </div>





```python
a = pd.Series([1, 7, 2])
a
```




    0    1
    1    7
    2    2
    dtype: int64




```python
a[0]
```




    1




```python
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
myvar
```




    x    1
    y    7
    z    2
    dtype: int64




```python
myvar['y']
```




    7




```python
myvar.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3 entries, 0 to 2
    Data columns (total 2 columns):
     #   Column    Non-Null Count  Dtype
    ---  ------    --------------  -----
     0   calories  3 non-null      int64
     1   duration  3 non-null      int64
    dtypes: int64(2)
    memory usage: 176.0 bytes

