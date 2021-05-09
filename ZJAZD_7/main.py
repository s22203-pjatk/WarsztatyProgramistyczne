import random

# #1
# # Z. Tuple (1)
#
# Stwórz krotkę zawierającą trzy imiona męskie (np. Zbyszek, Stefan, Franek) i trzy
# imiona żeńskie (np. Asia, Basia, Kasia):

names = (
    "Franek",
    "Marek",
    "Zbyszek",
    "Asia",
    "Basia",
    "Kasia",
)
print("\n")
print(names)
print("\n")

# #2
# # Z. Zbiór (2)
#
# Stwórz krotkę zawierającą trzy nazwiska: Studencki, Banach, Kowalski:

surnames = (
    "Banach",
    "Kowalski",
    "Studencki",
    "Pilicz",
    "Nowak",
    "Curie",
)
print(surnames)
print("\n")

# #3
# # Z. Pętla imion żeńskich
#
# Stwórz pętlę drukującą jedynie imiona żeńskie:

for kobitka in names:
    if kobitka[-1]=="a":
        print(kobitka)
print("\n")

# #4
# # Z. Funkcja
#
# Napisz funkcję sprawdzającą czy nazwisko wygląda jak polskie (czyli czy kończy
# się na -ski, -cki):

def zdacydowaniePolaczek(s):
    koncowki = ('ski', 'cki')
    for each in koncowki:
        if s.endswith(each): #szuka koncowki w nazwisku, jesli znajdzie to true jesli nie to false
            return True
    return False

# #5
# # Z. Pętla nazwisk "polskich"
#
# Stwórz pętlę drukującą nazwiska wyglądające jak polskie (czyli nazwiska kończące
# się na -ski, -cki):

for each in surnames:
    if zdacydowaniePolaczek(each):
        print(each)
print("\n")

##5
def filtracjaPolaczkow(zn):
    listaPolaczkow=[]
    for each in surnames:
        if zdacydowaniePolaczek(each):
            listaPolaczkow.append(each)
    return listaPolaczkow
print(filtracjaPolaczkow(surnames))
print("\n")

# #6
# # Z. Imiona i nazwiska
#
# Stwórz pętlę tworzącą pary (imię, nazwisko) używając zbiorów imion i nazwisk
# zdefiniowanych wcześniej i dodaj je na listę. Następnie wydrukuj każdy element
# tej listy:

people = [] #nowa lista

for n in names:
    for s in surnames:
        people.append((n, s,))

for each in people:
    print(each)
print("\n")

# #7
# # Z. Żeńskie imiona i nazwiska
#
# Pamiętaj, że polskie nazwiska kobiet kończą się na "a". Popraw pętlę z
# poprzedniego zadania tak żeby zachowywała ten warunek:

for n in names:
    for s in surnames:
        if n[-1] == 'a' and zdacydowaniePolaczek(s):
            s = s[:-1] + 'a'
        people.append((n, s,))
        print(n,s)
print("\n")

# #8
# # Z. Losowanie imion i nazwisk
#
# Napisz funkcję, która na podstawie stworzonych wcześniej zbiorów imion i nazwisk
# stworzy nazwę człowieka. Pamiętaj o odmianie nazwisk żeńskich!

def stworzOsobe(names,surnames):
    x = random.randint(0,len(names)-1)
    losoweImie = names[x]
    x = random.randint(0,len(surnames)-1)
    losoweNazwisko = surnames[x]
    if losoweImie[-1] == 'a' and zdacydowaniePolaczek(losoweNazwisko):
        losoweNazwisko = losoweNazwisko[:-1] + 'a'
    return "{} {}".format(losoweImie,losoweNazwisko)
print(stworzOsobe(names,surnames))
print("\n")
