'''
# Z. Moduły

Plik z kodem: `studentm.py` i `studente.py`

Stwórz plik `studentm.py` (student module). Napisz w nim prostą klasę `Student`,
której konstruktor będzie przyjmował parametr `index` i ustawiał go jako pole w
tej klasie.

Stwórz plik `studente.py` (student executable). Zaimportuj w nim moduł
`student`, utwórz obiekt klasy `studentm.Student` i wydrukuj go funkcją
`print()`.
'''
class Student:
    def __init__(self, index):
        self.index = index