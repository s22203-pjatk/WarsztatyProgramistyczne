# # Z. Figura: trójkąt
#
# Napisz program, który będzie rysować trójkąt o podanym kształcie:
#
# ```
# *
# **
# ***
# ****
#
# ```
# Niech wysokość trójkąta będzie podana jako argument na wierszu poleceń.

def trojkatRysowanie(rozmiar):
    gw = "*"
    i = 1
    while i <= rozmiar:
        print(gw*i)
        i += 1

trojkatRysowanie(2)
trojkatRysowanie(3)
trojkatRysowanie(4)
print("\n")

# # Z. Figura: odwrócony trójkąt
#
# Napisz program, który będzie rysować trójkąt o podanym kształcie:
#
# ```
# ****
# ***
# **
# *
# ```
#
# Niech wysokość trójkąta będzie podana jako argument na wierszu poleceń.


def trojkatRysowanko(rozmiar):
    for i in range(rozmiar,0,-1):
        print('*'*i)

trojkatRysowanko(2)
trojkatRysowanko(3)
trojkatRysowanko(5)