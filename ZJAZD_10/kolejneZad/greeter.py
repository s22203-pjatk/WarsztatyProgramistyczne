'''
# Z. Funkcja w funkcji

Plik z kodem: `greeter.py`

Napisz funkcję `greeter(greeting)`. Wewnątrz niej, napisz funkcję `impl(who)`.

Niech funkcja `impl()` drukuje pozdrowienie korzystając zarówno z parametru
`greet` (przekazanego do funkcji `greeter()`) i parameteru `who`.

Niech funkcja `greeter()` zwraca funkcję `impl()`.

Przetestuj swój program w następujący sposób:

```
hello = greeter('Hello')
hello('Ala')
hello('Kot')

greeter('Hello')('World')

'''

def greeter(greeting):
    def impl(who):
        print(greeting+who)
    return impl

hello = greeter('Siemanko')
hello('Ala')
hello('Kot')

greeter('Hello')('World')