# # Z. Klasa `Hello`
#
# Napisz funkcję `hello(person)`, która będzie drukować powitania:
#
# ```
# hello('World')  # wydrukuje "Hello, World!"
# hello('Test')   # wydrukuje "Hello, Test!"
# ```
#
# Następnie dodaj jej nowy parametr o nazwie `greeting`, którego domyślną
# wartością będzie string `"Hello"`. Jej nagłówek powinien wyglądać wtedy tak:
#
# ```
# def hello(person, greeting = "Hello"):
#     # TODO
#
# hello('World')      # wydrukuje "Hello, World!"
# hello('Test', 'Hi') # wydrukuje "Hi, Test!"
# ```
#
# Następnie napisz klasę `Hello`, która w konstruktorze będzie przyjmować parametr
# `greeting` (z domyślną wartością `"Hello"`).
# Będzie ona też miała metodę `greet()` przyjmującą parametr `person` i drukującą
# takie same napisy jak funkcja `hello()`:
#
# ```
# hello('World')              # Hello, World!
# Hello().greet('World')      # Hello, World!
#
# hello('Test', 'Hi')         # Hi, Test!
# Hello('Hi").greet('Test')   # Hi, Test!
# ```
############################################################################################################
class Hello:
    def __init__(self,greeting="Hello"):
        self.greeting = greeting
    def great(self,person):
        return print("{} {}".format(self.greeting,person))

def hello(person,geeting="HeLLo"):
    return print("{} {}".format(geeting,person))

hello("blaBla","hi")

new = Hello("hi")
new.great(":o")
############################################################################################################