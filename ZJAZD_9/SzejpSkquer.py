# # Z. Klasy `Shape`, `Triangle` i `Square`
#
# Zdefiniuj klasę `Shape`, która będzie posiadać metodę `draw()`. Metoda `draw()`
# powinna przyjmować parametr `n` będący rozmiarem figury do narysowania. Pozostaw
# implementację pustą... lub zgłoś wyjątek typu `NotImplementedError`:
#
# ```
# raise NotImplementedError('draw')
# ```
#
# Następnie spróbuj wywołać metodę `draw()`:
#
# ```
# s = Shape()
# s.draw(4)
# ```
#
# Następnie zdefiniuj klasę `Triangle` dziedziczącą po klasie `Shape`:
#
# ```
# class Triangle(Shape):
#     pass
# ```
#
# Spróbuj wywołać na niej metodę `draw()`:
#
# ```
# t = Triangle()
# t.draw(4)
# ```
#
# Czy to zadziała? Dlaczego nie zadziała i dlaczego w *taki*, a nie *inny* sposób?
# Wypełnij metodę `Triangle.draw()` kodem z zadania "Figura: trójkąt".
#
# Następnie zdefiniuj klasę `Square` i wypełnij jej implementację `draw()` kodem z
# zadania "Figura: prostokąt".
############################################################################################################
class Shape:
    def __init__(self, n = None):
        self.n = n
    def make_n(self, n):
        if n is None:
            n = self.n
        return n
    def draw(self, n = None):
        n = self.make_n(n)
        for i in range(1, n+1):
            self.draw_line(i, n)

class Triangle(Shape):
    def draw_line(self, i, n):
        print("*" * i)

class Square(Shape):
    def draw_line(self, i, n):
        print("*" * n)

s = Shape()
q = Square(3)
t = Triangle(3)

t.draw()
print("\t")
t.draw(6)
print("\t")
q.draw()
print("\t")
q.draw(6)



