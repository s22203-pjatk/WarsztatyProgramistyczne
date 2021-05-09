# # Z. Gra w zgadywanie
#
# Napisz program, który będzie losował liczbę z zakresu od 0 do 100 (włącznie).
# Następnie niech pyta użytkownka o podanie liczby i:
#
# - jeśli podana była zbyt duża wydrukuje "Za dużo!"
# - jeśli podana była zbyt mała wydrukuje "Za mało!"
# - jeśli podana była równa wylosowanej wydrukuje "W sam raz!" i zakończy pracę


import random

zakres = random.randint(0,100)

while True:
    liczba=int(input("Podaj liczbę od 0 do 100 "))
    if zakres>liczba:
        print("za mało...")
    elif zakres<liczba:
        print("za dużo...")
    else:
        print("gitówa")
        break