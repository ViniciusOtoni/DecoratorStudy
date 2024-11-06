# Decorators

É um Design Pattern que conciste na idéia de adicionar ou modificar comportamentos de uma função sem realizar algum tipo de alteração no escopo da função que está sendo "decorada". Ná prática, um decorator é uma função de alta ordem (função que recebe como parâmetro outra função) e retorna uma nova função com as novas funcionalidades.

**Exemplo**

````python

import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio} segundos")
        return resultado
    return wrapper

@medir_tempo
def soma(a, b):
    time.sleep(1)  # adicionando delay
    return a + b

print(soma(3, 4))

````

**Explicação**

 - **Argumentos Args & Kwargs**: wrapper aceita *args e **kwargs, permitindo que funcione com funções de diferentes números de parâmetros.
 - **Tempo**: inicio registra o tempo antes de executar a função, fim o tempo após a execução da mesma, por fim é feito a diferença entre ambos.

### Decorators já presentes no Python:

1. **@classmethod**

    recebe o (cls) como parâmetro ao invés do self. Permite acessar ou modificar o método da classe sem realizar uma instância da mesma.

```python
class Exemplo:
    contador = 0

    @classmethod
    def incrementar_contador(cls):
        cls.contador += 1
```

2. **@staticmethod**

    Define um método estático, não dependendo da classe ou da instância da mesma.

```python
class Exemplo:
    @staticmethod
    def saudacao():
        return "Olá, mundo!"
```

3. **@property**

    Utilizado para definir um método como propriedade da classe, assim conseguindo acessar o valor como um "atributo" da classe.
    { Get, Set }

```python
class Circulo:
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, valor):
        if valor > 0:
            self._raio = valor
```

4. **@functools.lru_cache**

Deixa o resultados da função em cache, assim evitando a execução para os mesmos parâmetros.

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def fatorial(n):
    return 1 if n == 0 else n * fatorial(n - 1)
```

5. **@functools.wraps**

Preservar metadados quando é criado decorators personalizados. Evitando que o decorator sobrescreva as informações

```python
from functools import wraps

def meu_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Executando algo antes da função")
        resultado = func(*args, **kwargs)
        print("Executando algo depois da função")
        return resultado
    return wrapper
```

6. **@abstractmethod**

Definir um método abstrato. 

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass
```