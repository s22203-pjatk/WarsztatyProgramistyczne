######################################################
# Z. Napisz klasę `Basic`
#
# Klasę (nowy typ danych) tworzy się za pomocą słowa kluczowego `class`:
#
# ```
# class Basic:
#     pass
# ```
#
# Aby dodać jej konstruktor należy zdefiniować w niej specjalną funkcję składową o
# nazwie `__init__()`:
#
# ```
# class Basic:
#     def __init__(self):
#         pass
# ```
#
# Funkcje składowe jako pierwszy parametr przyjmują wartość, *na której* są
# wywoływane. Konwencja nakazuje nazywać ten parametr `self`.
#
# Następnie dodaj do klasy pole o nazwie `field`. Należy to zrobić odpowiednio
# modyfikując konstruktor - przypisując w nim wartość do nowego pola w wartości,
# do której referencją jest `self`.
#
# ```
# class Basic:
#     def __init__(self, field):
#         self.field = field
# ```
#
# Następnie utwórz obiekt takiej klasy (użyj dowolnej wartości w konstruktorze) i
# wydrukuj wartość pola `field`:
#
# ```
# b = Basic(42)
# print(b.field)
# ```
############################################################################################################

# class Basic:
#     def __init__(self,field):
#         self.field = field
#     def __str__(self):
#         return "Basic {x}".format(x=self.field)
#
# b = Basic(100)
# print(b)

############################################################################################################
# # Z. Metoda (a.k.a. funkcja składowa) `Basic.print_field()`
#
# Dodaj do klasy `Basic` metodę `print_field()`. Niech ta nowa metoda drukuje
# zawartość pola `field` w klasie. Definiowanie metody `print_field()` wygląda
# podobnie jak metody `__init__()`. Różnicą jest to, że ta drukująca ma
# normalniejszą nazwę:
#
# ```
# class Basic:
#     # __init__()
#
#     def print_field(self):
#         # TODO
# ```
#
# Następnie wywołaj tą metodę:
#
# ```
# b = Basic(42)
# b.print_field()
# ```
#
# # Z. Metoda, a funkcja
#
# Zdefiniuj funkcję wolną (tj. nie przynależącą do żadnej klasy) `print_field(x)`.
# Niech drukuje ona zawartość pola `field` w wartościach typu `Basic`.
#
# ```
# def print_field(x):
#     # TODO
# ```
#
# Następnie wywołaj ją:
#
# ```
# b = Basic(42)
# b.print_field()
# print_field(b)
# ```
#
# Następnie spróbuj takiego czegoś:
#
# ```
# # ...
# print_field(b)          # (1)
# Basic.print_field(b)    # (2)
# ```
#
# Czym różni się wywołanie oznaczone jako `(1)` od tego oznaczonego jako `(2)`? W
# Pythonie nie ma zbyt wielkiej różnicy między metodą (czyli funkcją zdefiniowaną
# wewnątrz klasy), a funkcją wolną. Wywołania metod to tylko sprytny sposób na
# przekazanie wartości, na której metoda jest wołana jako pierwszego parametru...
#
# ...i na sprytne podjęcie decyzji, którą funkcję *tak naprawdę* wywołać.
############################################################################################################
class Basic:
    def __init__(self,field):
        self.field = field
    def __str__(self):
        return "Basic {x}".format(x=self.field)
    def print_field(self):
        return print(self.field)
    def __gt__(self, other):
        return self.field>other.field

class X:
    def __init__(self,field):
        self.field = field

def print_field(x):
    return print(x.field)


c = Basic(-5)
b = Basic(10)
x = X(":o")

print(b)
b.print_field()

print(c<b)
print(c>b)
print(c==b)

print_field(b)
b.print_field()
Basic.print_field(b)

print_field(x)
Basic.print_field(x)
############################################################################################################