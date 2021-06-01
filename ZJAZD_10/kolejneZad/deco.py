'''
# Z. Dekoratory

Plik z kodem: `deco.py`

Napisz prostą funkcję `printer(x)`, której jedynym zadaniem będzie drukowanie
parametru `x`.

Napisz funkcję `simple_decorator(fn)`, której jedynym zadaniem wydrukowanie
parametru `fn` i zwrócenie go. "Udekoruj" funkcję `printer()` dekoratorem
`simple_decorator()`. Dodaj do programu wywołanie funkcji `printer()` i uruchom
go żeby sprawdzić co się stanie.

Następnie napisz funkcję `debug_decorator(fn)`, która przed przed wywołaniem
funkcji `fn` wydrukuje jej nazwę oraz przekazane do niej argumenty.
Zauważ, że nie wystarczy napisać `print()` w dekoratorze, bo będzie on wywołany
*od razu*! Trzeba to zrobić w dodatkowej funkcji wewnętrznej w dekoratorze, i
zwrócić tą funkcję wewnętrzną.

Wydrukuj udekorowaną funkcję `printer()` i sprawdź co pokaże Python. Czy funkcja
jest pokazana jako nazywająca się `printer`?
'''

def simple_decorator(fn):
    #print("z simple_decorator",fn,"o co kmą")
    def impl(x):
        x+=1
        fn(x)
    return impl

@simple_decorator
def printer(x):
    print(x)

# simple_decorator(printer)
printer(3)
print(printer)
#printer=simple_decorator(printer) dokładnie to samo co @simple_decorator