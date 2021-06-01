'''
# Z. Rejestr funkcji

Plik z kodem: `fn_register.py`

Napisz klasę `Fn_register`. Niech zawiera ona jedno pole będące słownikiem.
Stwórz w programie obiekt tej klasy: `fr = Fn_register()`

Niech klasa `Fn_register` ma metodę `register(???)`, która do słownika będącego
polem klasy dodaje funkcję `fn` (aby dostać nazwę funkcji `fn` pobierz wartość
jej pola `__name__`). Zadbaj żeby można było jej użyć jako dekoratora.

Następnie napisz funkcję `printer(x)`, taką jak w poprzednim zadaniu. Udekoruj
ją za pomocą następującego dekoratora:

```
@fr.register()
def printer(x):
    ...

(*Inna osoba.*)

Do klasy `Fn_register` dodaj funkcję `call(fn)`, która umożliwi pobranie funkcji
przechowanych w rejestrze po ich nazwie. Powinno być możliwe wywołanie funkcji
`printer()` z poprzedniej części zadania w taki sposób:

```
fr.call('printer')('Hello, World!')
```

Zmodyfikuj metodę `register()` w taki sposób żeby opcjonalnie można było
funkcjom zmienić nazwy pod jakimi są rejestrowane:

```
@rf.register('p')
def printer(x):
    ...
```

Następnie wywołaj funkcję `printer()` w pod zmienioną nazwą:

```
fr.call('p')('Hello, World!')
```

'''

class Fn_register:
    def __init__(self):
        self.slownik = {}
    def register(self, name = None):
        def impl(function):
            nonlocal name
            if name is None:
                name = function.__name__
            self.slownik[name] = function
            return function
        return impl
    def call(self, name):
        return self.slownik[name]

fr = Fn_register()

@fr.register('p')
def printer(x):
    print(x)

print(fr.slownik)
fr.call('p')('hello (*^▽^*)')
