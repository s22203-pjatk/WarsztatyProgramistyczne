#####################################
#
# # Z. Program `echo(1)`
#
# Napisz program, który odczyta w wiersza poleceń wszystkie swoje argumenty i je
# wydrukuje. Dodać do niego opcje:
#
# - `-n`: nie drukować znaku nowej linii na końcu
# - `-r`: wydrukować argumenty w odwrotnej kolejności
# - `-l`: wydrukowac argumenty każdy w osobnej linii

import sys

term="\n"
rev=False
up=False
separator=" "

for i,each in enumerate(sys.argv[1:]):
    if each=="-n":
        term=""
    elif each=="-r":
        rev=True
    elif each=="-u":
        up=True
    elif each=="-l":
        separator="\n"
    else:
        break

arg = sys.argv[i+1:]

if rev:
    arg=list(reversed(arg))

if up:
    for i,x in enumerate(arg):
        arg[i]=x.lower()
    arg[0]=arg[0].capitalize()

print(separator.join(arg),end=term)
print("\n")

### to w terminalu jak co ##python echo.py -u -r -l ala ma kota