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

def trojkatRysowanko(rozmiar):
    for i in range(rozmiar,0,-1):
        print('*'*i)

trojkatRysowanko(2)
trojkatRysowanko(3)
trojkatRysowanko(5)