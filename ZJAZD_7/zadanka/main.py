import random

#1
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

#2
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

#3
for kobitka in names:
    if kobitka[-1]=="a":
        print(kobitka)
print("\n")

#4
def zdacydowaniePolaczek(s):
    koncowki = ('ski', 'cki')
    for each in koncowki:
        if s.endswith(each): #szuka koncowki w nazwisku, jesli znajdzie to true jesli nie to false
            return True
    return False

#5
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

#6
people = [] #nowa lista

for n in names:
    for s in surnames:
        people.append((n, s,))

for each in people:
    print(each)
print("\n")

#7
for n in names:
    for s in surnames:
        if n[-1] == 'a' and zdacydowaniePolaczek(s):
            s = s[:-1] + 'a'
        people.append((n, s,))
        print(n,s)
print("\n")

#8
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
