'''
# Z. Framework

Plik z kodem: `framework.py`, `app.py`

Stwórz moduł `framework`. Napisz wewnątrz niego klasę `Framework`.

W klasie `Framework` napisz metodę `route()`, która pozwoli na dekorowanie
funkcji i nadawanie im ścieżek (spójrz na poprzednie zadanie). Zadbaj o to żeby
używane nazwy rozpoczynało się od znaku `/`.

W klasie `Framework` napisz metodę `url_for()`, która pozwoli po nazwie uzyskać
jej ścieżkę.

W pliku `app.py` zaimportuj moduł `framework` i napisz przykładowe wywołanie:

```
app = framework.Framework()

@app.route('/example')
def example():
    ...

print(app.url_for('example'))  # example
#####################################################################################
zad.2
W klasie `Framework` napisz metodę `routes()`, która zwróci sekwencję, której
elementami będą tuple `('url', <function ...>)` reprezentujące zarejestrowane w
aplikacji ścieżki. Niech umożliwia ona następującą iterację:

```
for url, fn in app.routes():
    ...
```

W klasie `Framework` napisz metodę `run()`, która zajmie się uruchomieniem
aplikacji. Niech w pętli pyta ona użytkownika o podanie adresu URL i wywołuje
powiązaną z nim funkcję. Jeśli takiej nie znajdzie, niech wydrukuje liczbę 404.

W pliku `app.py` napisz funkcję `hello()` i zarejestruj ją pod adresem `/hello`.
Na samym końcu pliku wywołaj metodę `run()` na obiekcie `app`. Uruchom program i
sprawdź jak działa.
#####################################################################################
(*Inna osoba.*) zad.3

Rozwiń nasz framework o możliwość odczytywania parametrów z adresu URL.

W tym celu niech adresy URL będą zapisywane jako wyrażenia regularne, a ich
dopasowywanie nie odbywa się operatorem `==`, a funkcją `re.fullmatch()`.
Rozwiń metodę `Framework.run()` o tę funkcjonalność, pamiętając o tym żeby
przekazać odczytane argumenty do funkcji implementującej dany adres URL.

W pliku `app.py` napisz funkcję `user(who)` i zarejestruj ją pod adresem
`/user/([a-zA-Z0-9-_]+)`. Niech drukuje ona napis `user: ` i nazwę użytkownika
pod danym adresem. Uruchom program i sprawdź jak działa.
#####################################################################################
'''
import re

class Framework:
    def __init__(self):
        self.slownik = {}
    def route(self, URL):
        def impl(function):
            nonlocal URL
            self.slownik[function.__name__] = (URL,function)
            return function
        return impl
    def url_for(self, name):
        return self.slownik[name][0]

    def routes(self):
        return self.slownik.values()

    # zadanie 2
    # def run(self):
    #     while True:
    #         user_URL = input("GET ")
    #         for URL, fr in self.routes():
    #             if user_URL == URL: #zadanie 2
    #                 fr()
    #                 break
    #         if user_URL != URL:
    #             print("\tERROR 404\t")

    # zadanie 3
    def run(self):
        while True:
            user_URL = input("GET ")
            for URL, fr in self.routes():
                match = re.fullmatch(URL, user_URL)
                if match:
                    fr(*match.groups())
                    break
            if not match:
                print("\tERROR 404\t")