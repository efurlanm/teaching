# Seções 2.1 e 2.2 do livro-texto

Este Notebook contém alguns exemplos retirados do livro-texto.

- Seção 2.1 - Estruturas de Dados
- Seção 2.2 - Algoritmos de Busca

## Seção 2.1 Estruturas de Dados

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


## Seção 2.2 - Algoritmos de Busca

### Busca sequencial

![image.png](data:image/png;base64,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)


```python
lista = [52, 73, 95, 98, 99, 103, 123, 152, 158, 173]
procuro = 98
for i,v in enumerate(lista) :
    if v == procuro :
        print("Achei!", i, v)
```

    Achei! 3 98


### Busca binária

Os valores precisam estar ordenados.

![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAecAAADXCAIAAACvYg4aAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAgAElEQVR4nO3dZ3wUVdcA8Dtte3rvCYEQCB1CR3rHgiAIggXEXrCBqI8iPjYERbAidiyIiii9SIsQIBB6CpDe6/Yy9f2wPHljCMnOZiebXc7/x4dkmblzdpOcvXvmFkwQBAQAAMBD4O4OAAAAgAiQtQEAwJNA1gYAAE8CWRsAADwJ6e4AAPAeNbXa7CuFBUVlVVq2TIvZaNZiYw0mm9lK22ys0UKbrYwTzWpUMpLAVXKZSkUp5ZRCToYGacJ8+EANFh4aFB8bER8TSZKEy59Ouzl9NntPZllJqb5eZ6moMdTpzU4MklDIyUAflUYtS4gO7BRk7dcruX/vZBz3wo4pBmNIAGijcznlP+48k36mUGuw2h/BEIYTJIYTCGEYhmE4hiEcwzCEYQLPC4gXBIHnWI5j0L//ADGcVPqGKjRBBKloeFAQeJ5jBJ7jOZbnaJ5jGKuBthqQwNsPkFHkpGFJ993RPzEmqN2etUvsTstZ/e2RqjojhuE4QeI4geMkwjGB53me5VmW51mEkEzl7xMUjxNUC00JPMexNo6xWgzVjFWPEBo3uPObiyfJKW/rm0LWBkA0hmEu5xVnns89lcdcuFxZVWfCCQLHCITjOIZjOI4wDEPY9ScKAm9P1jzH+mrknaICu3UNiVLZOidEMyxXUlZVqZVl5JTlFtayPEEpNJRcQyl8SJmquaYEnmN4juYYK0tbWNrM2owhAaouccGDugcOSInu2jmOIDpuBzwrt2DTwdyte7NwnMRxCidIDGvuFeN5jmM4jkEIU/lHKH3Cmj2sCfsbm1lfQWH01NFdn5o9yNfHR4In4R6QtQEQIT3j/Na0ksMZ+WYri+METpD2vmGzOdpOEAR7N5njGIWc6JscOaZP6Mgh3UOCA1q40NX8klPn8s8Xmk9eLKnWsTKlD6XwlSn9MOyGH/kFQeBZG0ubbWYtYzP4q8lxwxP7xCgG9+8RGOjXpqftUnX12lc/OZB2upAgZSSlcCQLI4R4nqOtJkqhUftHUXINcuwsjrGa9RUBCuuDt/adPLqbSqVsW+wdAmRtAFqXeT5ny4GCg6fyDGaGIGQESbWQPRvwPMexDM/RSXHBA5I0E4en9ErpLPbSgiCczLyUUaDNPFt+KqtS4ROqUAcSlKLVEznGajXVMVYDLpinjEge1TtwcP8UuVwuNgAXEgRh3+GT6zZfKq02U5TCwcyLEBIEnqEtvbqEDuzq+/3uqzzp6xMU78iPwI4260zaksRI9dolE8LCQpwNv6OArA1AS7Jyy1dsOJB1tQrDcEqmxAnHiqSCQNMWnmOUCuqdZyaNHJDokmB2p+X856M9NMPJ1UE+wQkO9lJZ2qyrvMxzdNe44HXLpoSGBLokGCf8vv/iik/24gQlkzdT87kRgedtVmNkmM+vq+eqlIr80tp7X/yFlwWr/CNFXV1bntWni/8Xr88UGXWHA1kbgOaVlFX9sv34pr8LGA7DCYogKIcqqjzPszTH0QNSooYlKyaOGRwRFuzCqApLKtKOF+44npddqJVrghWaYIKUORAVR1u0NlO9HJnvHp8w97ZhAf7tXefNvlLy4Ot/WhmMIOUOvt8ghARBoK2mlM4hbzw6IiEuyv7gibNXnl21l6MC1P5Rjve4OZbWVebOHRPx3EO3OfMEOgzI2gA0lX2l4ONfzhw5VUAQFClTOJgXBJ5nWZuCQuOHdpk+Mr53ShdJgzySfmbL4ZKjZwpxRYjSN7Tl8RUNOMZqqi+hLfWThyY9MrtfbFS4pEE2KCouXfj6Dq2Jd+Q9poEgCLTNNHdc7AsP397kv85kFS5+d6eFU/qEJDr+HsBzjLYie2iviFcfGh4S7GHjbRpA1gbg/9E089WWjA2/n+R4JJNrHE8HLGtjaauvRv75y5O7JcVLGeO/nMwqevz1rTTL+wQlKDSOpiGWNuuqrmgUaNmDYyaP6CpphHbPvPvXoVNF4gojCNFWY3So5q+PH2j2gBqt8dbHv6V8YuVqETUfxmrQVmTPHN/zlUfGOn5Wh0IsX77c3TEA0CEUFpU/u3rXjkM5GCGjZCoHU7Yg8CxtDfIl503pu+zBYYnx0VLH2VhUiN/o/pFyueJKXoHFSlNytSOfDHCCUqiDbDSz6/C57Pyqvl0CNRq1RBFyHLfm+7Q/D2TJ5I6+pHYsbcUx7r+PjYyNav7+oUohiwwkd6VdkqsCcNzRQdkEKadk6gvZV1K7+rm2eNVuoK8NACopLdu4M3frgYsMRxCUrIVhfI0JgsAyVp6jZ41NeXL+UOkSnyOqa2rf+/rYnuNXVX4RKr9IR99yeN6sL6e4urmTet85LkmKosHar3d8tS2XkqsJB2/kIoQQ4jgmSEN8uGRc185xLR+5av3fP+y96B/WlZSLeP1t5npfrHrD8tvCQz2vTgJZG9zsdHrjnBd+KavRUzKlqKorbTOp5cQHL04bkBIjXXiibDuUteLTfZjc3ze4k+NnWQxVxtrCTtGBG9+ZpVK2PqbQcTq9ceyiLzFMQVAiXliEkM1qfOX+YTOm9mv1SIPRPOXRb22Cwi8sSdQltBXZ4f74bx/Mk8kcuiXQcUCFBNy8BEHY/fex1z7/p6TaSMlVhGM39BBCHMswNnOX2MA1z4/rlRwraZCiJMWHDOwWmHmpuKKignT4TYiSq+WqgNo6/YlzVztHKl04NPCjb9PO5dVRMjHvBILAMNbIYNWLi0bKZK3HL5dRI/qE7zuaw2IqUW+6BKmoqiyTCeb+PUW8w3UEkLXBTcpstryyds/nWy4YrYiSKR0fQMYytkAf7JUHbnl+wS1h7hv7fCPhoUHTRnRRUdjpc1msQDQ7G/56OEEp1IGVdeZNO05p64wDe0e3fTb8nwcurduUToktZ7M04un3nx0fH+vo+JagAL9AtbD7nyyFJtjxaxGkTKbwzTh3ZdLgWF9fjeMRup0XLogFgCPW/JC+J/2KXOkjqoPGsgzHWlc+PWry2B6O9ATdQq1WLZg56J0nxhlq8k31xcjBKiiGqfwiAiK7bfo76+Of0tsYQ1lF9asf7cFxhyaRNsaytgV3DujfW9wk0mnjBoT4kqa6YlFnUQqNQPn+si9H1FluB1kb3HQKi0qeXblt8+5zMrla1HQPlrERyPbGYyP69BBXQnWLYQM7L7s/VbDV6qvzhP+tDtgqUqb2C0vauOP8M+/+VVpW7vTVv9uShhDCxbwjIoQ4lkmMCVx4Z6oTV7xnYheLoYq26EWdpfQN++PvS1fzS5y4orvA3UhwczmbXbD43d16E+v49BmEkCDwtNWUFBf00oKhvVMSJI3QtYwmyysf7T16vs4nuJWVThvjWNpYWxCk4T9eOq5TQiujOK6XX1h215LfcFKJ4yLKLIIg0FbjR0vGDRvYXewVEUIcxy19f+fBzPKACHGnG2oK1KRp08qZwUEdrt7VLOhrg5sITTNLP9ivt/CUXCXqkztDW1M6h25afY9npWyEkEatXPnM5EA1V192kecc3ZOBIGV+YUl1ZurVz485cdFdxwoFRIhK2QghlrHGhPs4l7IRQgRBvLl4EoXRHGMVdaLCJ7hWa96xz5ln6haQtcHNguf51RsOVtVZSFLEuneCwNM2c5CffMXDQ6SLTVIyGfXuM2PjI3z0VVd5nnP8RE1gbHahYe6SHy9fKXX8LJbldhzJdnxAjh3PcxxLTx0SJeqsJuQUOXVMV4uhStRZpEwtVwfuOKn1lMIDZG1wU7h8pXTmMxs3H8gWNaTBXhjp3ino85fGO1Eo6Dh6J8f/+sG8GSNidZW5gsOJGycov/CueZXCQ29uy8svdOQUnudf/GBnaZXR0cUR/4djbJHBvvfcPkzUWddbdGtfzlrH0RbHT8EwzDe40+US077DJ9p49fYBWRvcFF7/4lB+SZ3j89TtWNqa0jl04zt3e3TKtsNxfMnDYyMDCVFdURwnfILjLbxm1cbTjhx/5sLlfelXxN6ERILAccyKp8a3fX5pWGjQgO6RhroicadhmEITePisto1Xbx+QtYH3e3/DX5eu1soUPpjje78KAsNY/TWU5xZGrofj+GuPjOTN1VZjjaPDARFCCKkDoo5fqFj6/g6trpURGodOliEMEzV5HSHEcWzfbpGummI6qm8YY9WzNpOos+SqgMOn8uu1BpfEICnI2sCbmc2W/6zd/f2ufEqhFpGyEWIYq4pCK58b6wW97Mb69+j0xmPDLNpCY72IsW44QfmFJe07UfzMe7ttNtuNDjObLb8fzJY5toJVYxxrmz7cZWvG3jauf6foQIu+UtRZBKWwcIrFK3ewLOuqSCQCWRt4LUEQVqw/9NdhcbVshBDL2DpH+/2+Zk7/FNfsQdOhjBvea/PKmeE+tNVQ4/hZBKUIjEy5VGT57xeHbnTMjiNnTDZO7NARjmP8NLJJYwaLOqsFCoV87dJJGG/gOXH5V+kbdjanfNffbZ1hJDXI2sBr/XPi3K4j2XK5RlQe4QWOZazPzu0dEuQvXWzulRAX+diMZJO22PHZNwghhGGaoLi/DmRdyLra7P8fO1fr+JDwBixtGdE/wbUTTaMjQ/t2jWCs4mbcyBQ+OEFlXBFxJ9MtIGsD71Rdq12z6RxJKUQVRnieoy2mmaO7DerfQ7rYOoKxIwYM6hmpLc/iWNrxs3CcVPtHfvhzJk03Hfqt0xtPnC8mHF7n2o7nWEEQUru4fuv0gcn+tFkn7hwMUwfEpJ8t4nkxb2btDrI28ELZuQV3PvNTXomepEQNzRYYm3nS8KTnHxwlWWgdBY7jrz8yMjlWY6jOEzVOWekXceaqfs6Sn8sr/lU4fnntPpOFE/UeiRDiOCY82GfCqIGiznLElNF9OJuW50S8JyGEFJqgGj33z4lzLo/HhSBrAy/07fYso4kWt0AoQjzHJET5v/PMZIVCRK73XKEhQd++dbefiqfNIka8YRjmExh3tbj2278uNTxYUlaVllkgdow2Qojn2IV3DpDLXf+ChwYHdIkLNGtFL6UiU/pnXBZXWmlnkLWBt8m+XLAv/arYOeuCwLOM7fFZfaULrAMiCPyJWb1NulJBTE2AoBS+oV3+PJRdVHwtJ6ZnnEcIOb4NmJ3A834aauotUm1c2TdRbTHWiL0nSSl9M86LmAva/iBrA69C08wbXxwVcEpUv4/nOZvVeNv4rmOH9ZQuto7pjgkDh/UM11ZkicpucpU/pgh96+tra3f8c8mM4wQucklujqPHDe3q2t1zGpswvDsSeNoirrpNyTWX8mvPZpVJFFXbQdYGXuX9745cyqshRS8QaiMw9LhTC4R6gfmTu7C02WoUMRAQIaT0DT1+vvSnnWcQQqeySkhK9B1FnudSokSMyBSrZ7dEfx8FYxM3cQbDMEqu+ebPUxJF1XaQtYH3OHDs4s87zxFi7kAihASBxxC/9uU7XLjzlmcZ0Kfb43OGWPQVotaWwjBc6Ru++pvDf+y/aDDRYjvaAkICx/Xv4+QKf47AcXzB9FTGKnq6I6XQHM7Iq6qplyKqtoOsDbwETdMrv00nKYXYjjZLW+8aFTOsj1fNgRQFw7BFMwfdNq6LScyESYSQyi+ckPv/d/1+J4Zp84ytS1xQbFSY2BNFmTu1T4AaF7t2q0zlz/HC3gMddLoNZG3gJf4+klFRaxI11A8hJAg8xzHzp7d1qTkvMH98d6ux2vEVARFCGIb7hiTyAiF2CjtCiGVtvZIixJ4lFkkSPZMiGFrcmiQkpSRIeV5tB927HbI28BLb0qsIQnTKpq2msYMTI8NDJIrKgyQmRKemROkqL4ubMImQwidUVGkFIcTznCAISRHtsZ51YhgpdiUphJBCE5yVJ26d7nYDWRt4g/W/HP8ns4gkxXWOWMamUVJPzRkgUVQe57GZPVnaYDVUizpL5RuGBCRqjqXAsQih4YN6i4vPKYN6xzlR2lb6huUU1Na3tsahW0DWBh7vcl7xJ5uOEaQMiVkiCiHEscwLD9wSFy3553RP0bdn11tHdRe7FwyGE3JNIENbHO+k8wIXHxXYPh9xenbvzIqJzQ7DCYxUZOXkSxRVW0DWBh5v+8GrCGGEyI42xzGJMQHTRnWTKCoPteSBEWF+MrGdU4UmBGGY491tnudvG91Or7xCLkuMCbQZa8WeSMrUWfmiz2oHkLWBZ6uprf9p73mZQvyazoztvtu64SLXzfB6GrXy/luTzTpxE8FJmdIvpDPL0o4saSIIgpzEZk1ov/W5+nePNOvKRW0EgRCSKXwuFIguiLcD+JUFnm3/4QyGw8Su6czzLEmgCcPao67qccYP78lY9Y5v6G4nU/mTlJLnW59gKQh8p5hAjdr16/zdSKSPhWNtPC/uGRGU8mqxuJlH7QOyNvBsR3MsYlcHFQSBsVkmDk1SyF25prPXCPD3Gdgz2lCTL3bPcpkqgGdbz4wCz8VHBjgbnTMSE6IRQqyYLYARQgQlL600dMA9ySBrAw924lzx4Yx8sXvL8iyDED9vSrJEUXmBmaOiaYuOtojb/VbpE8LzXKujAHmeS45s11UV+/ZIInBM7Pg/DMMxUrnlQLZEUTkNsjbwVLV19c+v3oYTMlG7iyGEWJZeOCO1a+ebdzJkq8aOSB3RP0Hs1os4QcnVgYzN1HInnee57l1ctkukIzQa1ZjBnRmbUeyJlFz90/YzHCduNLrUIGsDT3Xwn0y90SZ2O3BBEOQUtmjmIImi8g44jr/22FjWZhC1gitCSK4KEASh5eq2IPCJCa7Zjt1xE4YmiZ3XjhAiZMrqelNldZ0UITkNsjbwVEezzThOiL4PyTFD+sTJKdHr999sgv01vbtG0CK3XiQVPhhOtrDoK89z/j6KAH+fNgcoTp+kEJ5zaIhLYwQpRwgVlVRIE5STIGsDj2Q0mtJO51MylfiZNfSkgTB/3SHjUyNtJnHdTBwnfILieJYRUPP5keeYzrFBrohOnJAg/+gwX44V190mKCVCKPdqsTRBOQmyNvBIZy5eoVkkdpdCQRAwgR85tJ9EUXmZgb3ixW5zjhCSqwMxgrxRaYXnuMgQ3zaH5oyYcH9ezLR7hBBByjCcqKfdE/CNQNYGHinjQonY2ghCiOfY/inRMODPQYnxUaEBCptZ9DLTlMK32SKJveQdrBI3btpVokJ9OcYm9iyZwre0SuRe7xKDrA08UtqFOsKJNZ15dkgPN3w891A4jo/uE2SoKRC1fCtCSK4O5JqbpGNfDCQ2XOOa+ESK9rNwjLgh2wghuSboanHHmtcOWRt4nnqt4UpRrRM7ggs816NzqBQheat+3SMFnmVFJjuZwkfguetL2/asHRXhnvsKkRGhohYmtKPkmooa0UMGJQVZG3ieoyfPOlEeEQSeJFBK1wQpQvJWPbslIoREz0/BCYJUNDNPkhcQQuGh7vm4ExLkL3aaPkIIJyizlbVYRI8alA5kbeB5TuSYndjyimWs/VOiVar2W/7CC4SHBo0f0oW2iL4nSSl9WcbWZMEmQeAJHAsPdc/+nDFRYRwruq6NEMIpeUFxBxr8B1kbeJ6rJXVi95ZFgsCxTI8usJS2aLMn92Jps9izKLlaEPgmq1oLSAgL8qEo9+zsFRTgR+C82CHbCCGCkFXVdKCJNpC1gYdhWS6vpA7DxC7yxyGEuoSLG9wNEEJ9ukb6qnCxY+ZImQr972VvIAhClzh33g0O9lfxnOjSNk5QHWp6JMwQAx5mz9HLFisrV4rLv/b00b83rBjVvJMXir/bespia35OI8vxnNWg0IhIuCSlJCgly1i5RtVtnudy8msefPVXhJBaKXtxwdCIsOA2Rt5E1tWSD74/zvPNd6h1RpuMtNlnPDoOJ+Xf7ynec+rXZv83wFf5n4dH+vq038AYyNrAw+w9dlns5BpkX/siJigowE+KkLxAao+Y4kr9ik/2ypR+lPy6BCQLET3OEsN8gprZsNHAoXN5RsQaNq2eGxHm+n53t8To5IS87/48TSk0MkXTHzeuCCUI0aP1ZUrfOguqK236TmAza1natOKh0e2ZshFkbeBZLBbrsTOFuMjyCEKI57kR/eIliMh7TB/TPTsr55cDxTKVv9LHBeMjKYUPpWi63ghLmy3GmpfuS02IkqpU8shdqQSB/7zzfLMBOIGSa65/J2NsRt5as/ThsVPHdm/7JUSBujbwJOezrlpp1qmR2vzMyT2lCMlrYBj20hN3fvnqhFClwVRfKna/LkdYjbX1ZRcfmBw3c8pglzfeQKVSPj1v+PvPj6F1+WZdudgpQq0TBJupzlJ39f3nx9w1oSch9sZ4m0HWBp7kcl4xQk4sP8IH+SujQ/ylCcqr9O/d7YPnx9OmCn1NnmsTt8BzxtqCicO6Pnn/FBc2eyND+nZ95t7hpvoSk67MtS3bzFp99dW5U3oN6dvVtS07CLI28CR1Rh4hhCGxtyL5+AhI2Y6Ki4l464mRStysr8lrMnTPaYIgGGryI0M1by+e6JIGHXHn2O4rHhqtEPRWo8tGgHCM1awtmjOlz6I7+7uqTbEgawNPUqHHcZwUuzqrIPAJMbD8iAgTRvTe9vF9Y/qH6SovOzEL/Hqm+mKbRdslNhgXfyfZaQRB3Dax9/qXpyr5SkNNgRMTI5tgbEZdZe5L9/VbunCUG6drQdYGnqS0UudcUduP6FgLAHV8GrXyracmzBgWUFdyzqKvcrodnmO0FTlWQw1Jyn01ChdG6KAunaM+e2l8jzi5tiKnLe9AFn2Vtjxr8ezud06WsCjvCMjawJNU1BidWIEECUJwIFRIRMMw7MXHpr/wwAhjXeH1Y/gcZKovYax6Sq5EGPJRtesmvw06JcRtWDFzUEqosbbAuRY41masK3zhgVvm3znSpaE5A7I28Bg8z9dqzZgT60YhPjQ4QIqQbgb3TOv30oKBxto8m6lO7HRwm1lrM9XJ5Gpn3mtd7ZUHh8SEkKb6ErEnCjynr7p6/5Qu90zrEPtpQNYGHqO0vJrlBLE7siOEBJ6PDIddx5w3a+rQd58YjltLDQ7fnxQEwaKvNFTnUXLVtaKWIBCcO7cXiIwI/+zlKfHBXH3ZJcdXVuE5Rld1ec7YxMULp0oanuMgawOPUVFVK/Y+pJ0gCKEh0Nduk7HDe/26Zp6fnDZpSx05njbXG+uKCJJs3MvmadFrB7pWSHDQysXjKJzWVzs0rlHgOV1FTkww9cyCUZIH5zDI2sBjMAwjdszf/wj+vu7ZP8WbBPtrPnxhohozWA01LR/JsTZjXRFByhqv+CEIiKLcPxk7OjJ0ywd39+sapK/Ja7ngIwiCviY/2I98/ZGR7Tn0pVUdKBQAWmYwWZxI2gLPKxVU+09g80rdkmI2vDqJNhTpKi/faK1qjrXpKnNxnKBkyn+XswSVwj13I5sIDw36cOnUQd386krO3nDpcEEw1OQPSQn4c929PbvFtW+ArYCsDTyGwPPIqb422ZE6Sp4uPi5Go5LTFq2+6ur1RQaeY+pLLwgcQ1LNJGgnlv2SiEqlfOupCQmRvobqq82M4xYEfU2eTDC++eR4mcw9q4G3oKO8iAC0Sqc3OZGzBcQr5e7/YO5NaJqTydU8azPUFjS+OWmfAIkQImXNzkARfNSq9oqxdRq18qeVd08c1ll/XeI21hfjnGH5I8M16o648xFkbeAxLFabE31tQRBIEsojLoZhOCVX0RZtXfFZm1mLEEKCYKwtYGmTTOnT7Dg/QUAd7Qchk1FvPjVhxvDY2uKzVuO1eVgmbWliKLb5vbvGDuugy41B1gYeg2EYZwokAvJRd4hyqtewMSyGYRiGUXI1wjB99RWOpY11RVZjDSVrabsKtcoNcyNbhuP4kofHzpzY01CTx9IWi77Soit7/ZHh0ZEuWKtWIvDJEXgMs8Uq8BzLiNstm+dds/4RaEAzHImu3YrEcVzgkbb8Es8xGEa0MGXc9SumugiO4688NEaFmTbuzeE55rl7+iYmRLs7qJZA1gYeo1+PTgzrzF9+TFTH7Td5onljmm4bxuJqkje1emK3LrHSROQCzy66NSI0LSk+qH/vbu6OpRWYEzsWAwAAcBeoawMAgCeBrA0AAJ7kWl27rKxMq9UqFFLd4a2trVWpVEqlJIMfBUGorq4ODZWqdknTtFar9ff3l8lE7+7sCLPZbDQaQ0JCnFgXyREWi8VsNgcFSbUtgFarxTDMz0+q7c+NRiOGYWq1WqL26+vrVSqVXC7VOJOamprAwECJpkRzHKfVaqX74VqtVr1eHxAQQFGSTDYxGo1ms1m6P16TyUTTdECAVKvQ1NbWymQyHx8X7CncLIPBEB8f3+SP61pd++zZs7m5l51Yb95BtM1KkhQu2axi2maRyaUaD8/zPMvYSEou2R8ey7GMhPFzHMsyMrlUb8kMbcMwjKQkeUtDCLEsQ2C8jJLqc6HFxuEEJd1SorTNQskUEr0lC4LA0Dbpfrg8x7Iso5ATBC5J/DaGZ1leul9+jmUEnlUqpMpsZiuLYYSEv/wMPWzY0Ojof41pufZkZDJZdKeU4LAYia597sS+yLiuErXPsUzmsV29Bo6TonGEkEFbk3P+WGJyPx//prfOXaKyNK8472JKv5EEKUl3pqayuKwwR7rXJ+fcUYKkOndPlaj94ryLIWpdzySpupP7jxX7hvXwDwqXqP3Mozu79RkuUWKyWc05545K98OtqSwuyD0zamBUgJ8kbwynL1bl5Guli7+sMMeiLZx0i1QLify5P1/hG56Q1Eei9vNzz1z/KQfq2gAA4EkgawMAgCeBrA0AAJ4EsjYAAHgSyNoAAOBJIGsDAIAngawNAACeBLI2AAB4EsjaAADgSZyc6Jl2aH/mqeP3P/i4j6+LV58oKy0+mZ5WVJgfG99p5OgJ/gGBLm6/pHjXjj9MRkNsXMLU22aS0qyucOFc5oF9OydPu7NzUrILm62qLN/0w9cN37q8fYQQyzBnz5w6m3mSZZmkrt1HjZ3kwsY/WbuSY9nGjyx8+CmVWuOq9nU64zh5VyEAABvmSURBVN4Dx7MvFygV8oljh/TonuiqlhscPXLg1MljsXEJE6fcoXDdujpph/ZbbdZxE6Y2PGI2Gf/6Y3NVZXloWMStd9zVlleJZZitv/9MUtTtd97d+PGzmRmHD+yZMfveyKg2bQJgsdq++HpL/77dhg3ubX+EYdj9B0+kZ1xQKuTTJo9ISe7UlvarKsv/+O2n3n1TBw0ZYX/EoNft2flnWWmxn3/AbdNntzFLHM+4sHPv0QXzb4uN/tf8WJ3OuG79Jooklz5zX1vaLyst3rZ185x5CxuyZZM/BLF/Bc5k7QP7dj78wCyE0IzZ812btXNzLk0bNyg0LMLfPyA359LEKbev+3yjC9tHCM26Y6y/f4BMrrhw7rRWW3/fwsdc2z5CSKfT3jn1FrlcERvfybVZtbio8LuvPu3VZ4D926EjxriwcbuVb/3nmw0fJ3XtjhDKzbl0MP1SZJTL1iE4f/Y0bbu2B0phQV5RYd6c+QtdmLUXPvHGb1v3p/brXlpW/fzLa7ZtXjN14nBXNY4QWv7SMz9+v2HAwGHrPnj7268++/HXXW1P3FaL5ZN1Kz9bt2rG7PmNs/bSZx9J/+dQrz4DTqSnnck8+faqT5y+xKp3Xvtq/boRI8c1ztoXzmXOu2uyzWYdOmJMG7P2vQ+99usf+95d8VRD1v50w69LX1s3cli/8xevrP3053PpPwcFOpkodDrt3BmTigrznnxmWUPWXv7ys8ePHemanHIiPe3k8X/akiUyMrNGTXnYarWNHz2oSdb+9sdtb773ldVqa0vWbsiW026/qyFbrnnvjREj/38SP/PvrkyrRGft3Tu2fr1+3cKHn/7y8w/FntsqjcZ3/TebBw8bRRLE5x+//9Gad+rragMCXbkAxYq314wZPwUh9NlHq3dt/0OKrP3tho979uoXGS3Joispvfp+uXGLFC0jhIoK8/fv3fHT73t79+lPUlRNdWVwSJgL2//0y58bvp5z5/jBw25xYfs6nXHr9oPn0zf16J5YVV03dNyCP7YddGHWPnrkwI/fb3h71SczZs/fv2fHowtn79u9bdodd7Wx2Tdefd5qtS58+Gmttq7hwYzjRzOOH9118HRQcMiV3Ky7bhvz8OPPxid0dqL9uTMmBoeEjZ0wteH9EiGUdzX31WVPP/b0kg9WrmhL8DW12sFj7p82acTg1H9tjDtoQI/Ci3+FhgRWVdf1GDT7lRWffLpmmXOXWLL4oQUPPbn85WcaPzhj9vw33/tYoVCcPpl+z12Tnf5Fzc4teHTxW68sWfjKiqZvivVa/Vff/zn3rolfff+nc5EjhK5czv78o9VrP/v+nTdeavJfbfkrFl3X7p86eOPmncndezh9yRZERkWPGjtJoVCQFDX7nvs5jqVpW+uniWFP2Qih6BhJNkMqKsw/cnDfD7/u0vj4StG+pH7/ZeOMWfP7pw62F45cm7Ibu3ThbFVV5SvLV7qwTYLAlQp5YXG5/VuLxZYQF+nC9k+dPIYQGjJ8FEJo7IQpsXGd0o8ebnuzS195c/W6L5v8Qb343KMjRo0LCg5BCHVO6tY5qdvX6z9yrv1Vazes/ey7JjWEoODQH3/bM3DwCKfDtlOrlScPfbfm3ec0GlXjxwel9ggNCUQIhYYEJiZEl1fWOH2JVR9+MffeB5s8OHT4KPuy0lFt+ysOCw08vHvDqOH9mzyu0xlHTFx0z+zJMdFtWlMsMjJ64+adk6beQbp0YTjRWTs4JEyiWnAT+3Zvl8sVYeGu/MNroK2v+3r9R6NdWrS1+/KzD+c98LALK55NXDyXuXDe9EcX3v3PkQMub7yystxsMiycNz0pxmfujInFRQUuv4Td75t/GD12kmtfJY1GtfDeO6bdtfiFVz6cOX9pZETI4sfnurB9uUKBEGroRsTFd6quqmh7s75+/tc/WFSYFxMb3/BtYGBQSXGhc+03W+Dy8/N3yWL6SoU8wL+V3smZ87mTxw9z+hIt12A/W7fqllHjnO5eBPj7KhXNrKv+6Ze/lpVXP/5QWz9IqdSaG2XLhfOmL5w3/aeNXzrRbAcdQ3IlN+vN5Utn37PA5S1v/e2nccN7D+wVp9PWT5o23bWN5+ZcOpN5cvzEaa5ttkFEZPTMu+/t0y81Mir6+ScXbvn1R9e2X15WcujAnkFDR7z34RdKlWrKmNTsrAuuvQRCiGWYIwf3SvEqLX58zoC+3b/8bmt2bsGi+6dTpCtXVb5l9AS5XPHGqy9s/f3nt19/8UR6mgsbb1lgcEi7Xcu1vvhmS7eu8fPnTHFtswX5V8YN753aI+aP3366e56Ls4TFavv51z17tn6sUkq1avkDi57s0y81OaXnN198NG547yu5WaJO74h7tNfWVD/zxANz5i98dulylzd++4w5t8+Yo9Npd/z524ypIw8dv+Squ2GVFWUzpo6cMOnWvbu3IYQKC/IoipLLFZOm3uGS9hFCkVHRS1950/71gIHDPvto1fSZruxOqpSq6Y8stt+z6t13wIRb+h49ciC5m4urYYcP7pXLFYOG3uLaZquq6ybe8cSzT8ybP2dK5tnsh55662Baxo9fvumq9pO79Ug7dXnfrr+KCvKGjRybdvjv8IgoVzV+PYNB3/B1VWVFs13yjoxh2E++2Pzpl7/u+G2ty9NffELnfWlnEULHjx5+4qF5jz71woKHnnRV42s//TksLDA7Jz87J//chcsIoY0/75hxx9hme+XOWfbqW/YvFix6ckjfTj9+v+HVN1Y7fnpHzNqr3nktPqHzS6+9I90l/Pz858xf+NpLi7MuXeifOtglbep0WpvN+tfWzX9t3Wx/JOP4Pzv/+t2FWbux0LAIlmFc26ZfQGBlRZn9a5lMjhAiXdpdtdu7e9s4CTrah//JjIkOf+iB6QihoYN6f7Zm2W2zn3XtJfz8/GfMno8Q0um0l3OzZt/zgGvbb9CjV7/amuqGbyvKSqT7ACeRTb/tWfzi6jXvPNcpXsL3tkFDb0np1eedN15yYdYuq6jesz99z/70hkfmP/TquNGDXJi1G9hvXXAsJ+qsjlUhMZuMb73+4oVzp5e/+YEU7Z86mX7uTIb96zOnTxIE2Smxi6saT+raPbfY0PBvxuz57334xckLxa5qHyF0OuO4Qa9DCLEM89um7/sOGOTCxhFCffqmHjm432qxIIT27PwTIdS3v4svodNp9+3aNmHK7a5tFiGkUMiKiisqKmsRQharbev2Q7Ftu5XUhNVq1em0CCGWYT764O3QsIhxE6TKpDNnzz9+7Ig9cWdfOl9XWzNu4tRWz+o4cq8U/fe9L9e889xji9paGm7Wnp1/2rss2vq6grwrc+YtdGHjH777vKDPsP97bdlDCCFBnxEe5rKRbAV5V4oK8+1f//bLRoRQ6iBxdX/RPaltWzevee+/JqMBITR3xsSBg4evXLNebCM38ve+Xd9s+DgoKGT2HdcGMy56dLELezRyufz9d18vKsxDCCNIYt3n37t2WGEThKv34SwquLrsuUc5jmNZpn/q4DfeWeva9m+fMedo2oERqUlqjU+nxKSfft/bs3c/117i0QWzu/fo5fKqC0Jo4tghO0cd7T9iHkkRCKFeKV3WrVriwvZLiguefuRek8mIEBo1duIfO4+4ZIzNK0ueTD962GQ0WK2Wk+n/9BswaOWa9XPvfdBo1N8+aZhCoSQIYs0n3zh9rTun3qLX6WprqliWHTe8970LHrl3waNXr+Q8fP8sq9WCEHr60Xs7JSZ9t2mbE41X19QPGfsAQqi0vPpUZtb6r39f9ebiO6aNeu/D78rKq9d9vmnd55vsR275aVXP7s6MXFx074z8vCsIoe+++mzr75t++HVnWHjkgX27Vr75H4QQyzKz5t7/2FNO/qCzcvJvnfWMxWpDCM2678XkLvH7t33a5BhFG7rYudkXH3twLkKotKSoIVsajYZXlz2t1+lYlomOiVv/zWaxc9mu7fablZWlNSOP3jdywIhbpWgc/W/fyK49h0i6b2TfIZNg38hmecG+kSn9R3n0vpGTRsRKum+kdH+8XrBvZO+ULmFh/3rP7lgVEgAAAC2DrA0AAJ4EsjYAAHgSyNoAAOBJIGsDAIAngawNAACeBLI2AAB4EsjaAADgSSBrAwCAJ4GsDQAAnuTaQhksy9ZVVVpM+paPdhrHMnVVpRK1z/M8Qqg476IUjSOEaJsFIVRVXqCtq5SifZNRhxAqKcjGcUneRC0mA8cy0r0+NosJw3Hp2jdoa1mTjWHErYsmon0TQ1cUGXS1ErXP83xZYS4hweqJCCGOZST94VpMBoRQVl69QkZI0X5VrQVJ+cdr1NexNvb0xSqJ2qcZjjPUSxe/yVDPcU1/86/9JuE4ztImC+/i7b4aEISE7QuCQJKkxeD8Lkct4ziOJEnaoudokxTt8yxLkqTVWIthmBTtsyxLELh0rw9CPBIE6drnOdrMY+W1vETtczzO2Iw8a5GofZIkrKY6id6SeZ6X9IfLsixJkrU6Acclef1pGpP0j5dnGQER0v3yYDiJeFbCPy6eVV635dO11aMAAAB4BKhrAwCAJ4GsDQAAngSyNvA2RpPFaJKqSA0cUaM1ujuENqmqrnN3CC2BrA28itFkeWntnpfW7oHE7RY0TX+15cTMxRuPZea4OxYnlZaVL1y+9bE3tpSWlbs7lubB3UjgPY5l5iz78ICZVSCEVKT17adHD+nb1d1B3URomn5+9c6008VKv3DeXLXorgHzpvaRyWTujkuEU2ezlq9Pr7EoOdoS5oc+e3lSVGSEu4NqCrI28BLHMnOefW8/rgpV+oYhhCz6St5c9f4LYyFxtw/7p5z0i/W+IZ0wnKAtekP11eH9YlY9N9lTEvfnP+z59PdL6oBolV8EQsisKw+UG5Y/NLh/727uDu1foEICvEGN1rjswwO4KlTlF4FhOIbhKr8IXBW67MMDnl5j9QhGk2Xess1pp4vtKRshJFP6BkT1SDtdvHH7GXdH55BTZ7M+/f2SJjDWnrIRQiq/iEodWrhi96mzWe6NrQli+fLl7o4BgDY5lpnz8Ot/mlmFJjCm8UwlUq42Ggxb9pzuGucTEyHJTs0AIUTT9NI1u89frvYJSSRl/z8lBMMJUqY+efoSjgspiSEEIcnsSpewF0Y4KkTl969NnymFD8dYMy6WjOwb7uvj467wmoAKCfBsjQsjGNb0s6Mg8FAqkVSTwsj1B3T8UkmTwsj17KWSjlPjhgoJ8GBNCiPXHwClEkldXxi5XgcvlVxfGLmevVTy5pfp7RlYCyBrA091LDNn5uKNZlZhv/3YAqVvmJlVePRwtA6IpumX1u4pKtf7hCTeKGXb4QTlE5L4xeaMjvb62wsj6oDoVn+FNEHxxy9UdJDhgFAhAR6p5cLI9aBU4lqtFkauR1v0tDa/4wwHbLUw0gTH0sbago4wHBD62sDzGE2Wlgsj12tcKoEJOG3kSGHkejKlL64KXbvxaEcolThSGGmCIGV+YUkdoVQCY0iAh7H38nIKanCCpC062qylzVpKrrlR+uA5xlhXZD+M52iT0XCluG5EvziZjGrnyL2DfcTI2ZxynJRzjMX+wgo8T8pUzR4v8JyxtrDh9ecY69ns8pREPzeO6rEXRgxmDscJe2C0WYsTMoJs/hMAYzOZtaXXngLPFZZUncst79PF312jSiRZqR0AiQiCcCzj/LBk1bDklIYHP/glRxAib3wKj2jtM7MaqiIRCKFjGefH3ZIq0YLm3q2ktKrJ659+vjQ934RQULPHC0iwGmtG9/Yf3DMKIWR//asrK3m+i0RrjrdMpzdcySuZNy664ZFqHbvhrxyZyh8hdbOn8BwdH4JNHxba+MGi0hp31UkgawNPgmHY+JEDmzz40e9XWj6LIonZ08dLFtTNpVNCdKeE6MaP6A1b0vOtLZ/VPd6vg/wI/Hx9mkRyIevqhr9auU0aEeLbQeJHUNcGAADPAn1t0LG899UhsadYabblErWVZp1o9oUFI8We4gWceKGy89hWj0nPZbUiWx6QpB49fIDYYA6kZWTkitspsF5vbvWY3IIaJ14Z555CqyBrg47lh+2ZBCkXeRKJoRtWqDGE8Yj8efclUS1yrO3mzNo/bM/EcALHxWUGheaGtxYxhBGk/MzlmjOXRWyuyPMsZglwIuWdOpv948F6sfETpLyFwUgYhlfUWp34FcIswZC1wU0hMLqXC1vDSZkTDVYXnHRhDJ5F6Rum9o9yVWsYTjjx+pu0pQjRzl3RtfEjhGRKvw71KwR1bQAA8CSQtQEAwJNA1gYAAE8CWRsAADwJZG0AAPAkkLUBAMCTQNYGAABPAuO1gfcb3D1g8czOQX6yJz88m10EO9q0q+dmdx7ULcBHRSGETuXUb9heWFDR+lzEjiM0QP7obQmp3fzlFGGyckcv1H6w+QrDunNbAuhrAy+3YkG3NxZ2D/Jz/zL8N6c+iX4/7S+ZvOTor4dKB3UPXP5AsrsjEmdYj8DoUOXzn1xY9F6m2caNHxA6qFuge0OCrA282fCeQZ2j1F/vLDydq3V3LDep+W+d2nKkHCH05fbCOj0dFayMC1O2elbHseVI+aL3MrOLjAUV5kUrT9sYLtjdPQCokACPtPu9od/sKpo+IiLAR1anp7/ZVWS1cY/cnhDoKzOa2eXfZJ+9qkMIpZ2vTTtfixDqkeDr7pC9yjfL+lVraYbh+yb54xg6nlX/0Za8e8ZFjxsQKiPxrELDsvUXTVauyVkMxyOErn+8/SXHat5Y2P2rHYV3jY6KCVGarNzWtDK9iZ0xMjLIV6Y1Mhu2F+zNqG5yVudoDYHjBnPrq2VJCvrawCPhOHbvxNjt6ZX3/DdDLiOendV5ydyk7/cUz/tvhsHCPjgtzt0Ber8+nf2C/GT3v33qi20FQ1ICv1rSb0hK4APvnN6aVt4tzueW3k3Xk1IriLAARV65qUbn5AIjruWvoZ6d1flivv7JD8+SODZrdPSD0+KPXqib/9YpksSWzEkKDfjXKmazx0S9ubB7vYHef7ppNm9nkLWBp1qz+cq3u4qq6m1/HS1HCG0/VrHtWEVlve2XA6XhgQp3R+f99CZm6ecXK+ttvx4q0xoZlhde+uJSVb3toy15V0qNgb5NywiLpsXrTMzbG3PdEm2zPv8zf/WmK9lFxtW/XCYJ7MvtBR9tyauqt21NK0cIJcdq7IfNGh21d/WwB6fGy2X40Qt1FOnmLZCgQgI8VWHltaEItToaIXSxQG//1mRl3bGz1U1HZ2K1Rsb+tcHM4ji6UnptYet6A4P/O7PdOiR8XP/QZV9c7FADSH49VGb/4kBmzUvzul7Iv/YrpDexCCHif8/hlwOlvxwoDQuUpyYHLJgc56+h/vt9K3vfSAqyNgBAWqP6BD82vdNP+0vO5+ndHYvzKuts245WxIQoR/d12z7FdtAnAQBIKDXZf+ncpHNXdT/tL3Z3LC4QHii30Lx7Y4C+NvBmUcGKMf1CEEKRwQqE0ORBYanJAd/v8Yb04RHiw1XLH+iGECqpttw95toewWcu687ne0yne8OSvjiGnciuRwgNTA6ICFK89/Nl94YEWRt4Kuv/ujwsLyCEGqarNZ63lhChvndibMO3UwaHI4Qga7sEw/L/+rpRIdtiuza2TyHDZSSOELptWETD/3JcYUfI2iwnNPm2yW+U3YMrM1cs6DZtcLhchpfWWNZsvvK3u8eQYILgzqmZADTRZ8aakPhUd0eBqgtOnvltsbujcIM+M9ao/CNdu4OXE0za0jv70c8/Pk/sias+3vj7aZnb40cIVRecnDcm2Imn0CqoawMAgCeBrA0AAJ4EsjYAAHgSyNoAAOBJIGsDAIAngawNAACeBMZrgw6nuuCku0O4qZm1ZWZtmbujQAg5OXG8w8QvFRivDQAAngQqJAAA4EkgawMAgCeBrA28DU3TNN0hdksBQAqQtYG32bj9zMbtZ9wdBQBSgTEkwHvQNL1x+5kvNmfYv503tY9M5ubttAFwORhDArwETdPPr96ZdrrYJyQRIWSovjq8X8yq5yZD4gZeBiokwEts3H4m7XRxQFQPmdJXpvQNiOqRdroYSiXA+0CFBHi8hsKIT0giTlD2B3GC8glJtFdLoFQCvAlUSIBna1wYkSl9m/6vRQ+lEuBloEICPFvjwsj1/wulEuB9oEICPFWzhZHrQakEeBmokACP1HJhpJnjoVQCvAVUSIBHarkwcj0olQCvAVkbeJ5jmTmtFkau11AqOZaZI11sAEgNKiTAk9hr2et/OWGl2caPh8SntnBWkwW7FTLyoVkDocYNPBRkbeDx+sxY02rWPvPb4naLBwBJQYUEAAA8CWRtAADwJDBeG0hlysNfuTuE/9duwez4fEH7XAjctCBrA6mU1ej9w5Pb4UL+4ZGtHZBsboc4ENJWZLfLdcBNDbI2kBCl8HF3CAh1mDAAcAmoawMAgCeBrA0AAJ4EsjYAAHgSyNoAAOBJIGsDAIAngawNAACeBLI26NAmDwob2y/EkSPnjY/57Nk+N/rf2FDlHcMjOkWqXBcaAO4BWRt0aM/O6vzY9ARHjpw5KuqrHYU3+t9+Sf6PT+80rEeQ60IDwD1glg3o0L7YVsCwfKuHDe8Z9Pmf+Sey6290wIV8/Xe7izJytC6NDgA3gKwNOjSa4Vnu2mLCybGa0AD5qRztqL4h/hrqconxRNa1NE2RmEZJNJwVG6pM7RagkhO1enpHeiVCyN4Ix///usSj+wZHBitxDNUbmAOZ1SYr137PCoA2gKwNOrQ7RkTwPNp2rAIhlBzrM3lQ2JK7k+QyHCHEcsK7P+YePFODEBrdNyQlwWfzwTKEkFpBrH26t1pxLYnPmxA7d8XJhAjVvRNjDWY2t9ioVhDvP9GzU4S64SoDuwW8+lWWG54eAOJB1gaeJD5cdSpX+83OIpOVXfd078fuSLBn7cbuGR9jtXGrfr58PKvult7BT96Z2DlK3fiA6SMiO0Wotx2r2LCtACF069DwBybH3TM++oe9Je32RABwGtyNBJ6kvM760heXckuMpTXW7CJDgI8sMkjR5Jhbegf9drg07Xwtwwr7T1Xf8XL6lVJT4wPGp4bqzcwnf+SZrJzJyv38d2m1znbXqOh2fB4AOA+yNvAk/HU3Jn3VTT8vKuUEw7a0r55GSRjMbONjaEZoqKgA0MFB1gbeRmdkVfKWUrDOyEYFKxs/olESpTUWieMCwDUgawNvcz5PP3VI+MDkAIrExvYP+fE/A5JjNY0POJVTjxB68s5OagWhVhB3j4lSK8kN22441huADgXuRoKOjm80XK/x1/Zx3A3jAhuKJ1/vLAzypV69L1kuw8trrb8dLrtaZooIUiCEeEFACK3fVmCwcOMHhNw2LAIhVFFnXfnj5bTzte30fABoG0wQWqoAAuC0PjPWhMSnujuKdlVdcPLMb4vdHQXwclAhAQAATwJZGwAAPAlkbQAA8CSQtQEAwJNA1gYAAE8CWRsAADwJZG0AAPAkMMsGSKi64KS7QwDA28AsGwAA8CRQIQEAAE8CWRsAADzJ/wFmTa+/HRky0gAAAABJRU5ErkJggg==)

A primeira coisa é ordenar a lista:


```python
achar = 152
lista = sorted([ 103, 123, 152, 158, 173, 52, 73, 95, 98, 99])
lista
```




    [52, 73, 95, 98, 99, 103, 123, 152, 158, 173]



A lista tem 10 números, vamos divir em 2, e iniciar em ~ 5:


```python
i = 5
lista[i]
```




    103




```python
achar > lista[i]
```




    True



O número que queremos achar está entre 5 e 10, vamos dividir por 2 de novo, e pegar ~ 7


```python
i = 7
achar > lista[i]
```




    False



Ele não é maior que o valor da lista[7], vamos verificar se é menor:


```python
achar < lista[i]
```




    False



Ele também não é menor. Se fosse menor poderíamos dividir o intervalo de novo por dois.

Neste caso como não é maior nem menor, então só pode ser igual, ou seja, encontramos o número.

## Exercício

Melhorar o algoritmo acima, deixar ele mais automatizado. Exemplo de solução possível:


```python
achar = 123
lista = sorted([ 103, 123, 152, 158, 173, 52, 73, 95, 98, 99])
lista
```




    [52, 73, 95, 98, 99, 103, 123, 152, 158, 173]




```python
l = len(lista)
i = int(l//2)
```


```python
while True :
    if achar == lista[i] :
        print("Achei!", i)
        break
    if achar > lista[i] :
        i = (l - i)//2 + i
    else :
        i = i // 2
```

    Achei! 6



```python

```

<br><sub>Last edited: 2025-05-13 13:25:43</sub>
