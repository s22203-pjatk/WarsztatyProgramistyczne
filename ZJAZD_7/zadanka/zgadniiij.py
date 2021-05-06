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