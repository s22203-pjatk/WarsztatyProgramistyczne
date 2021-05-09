##############################################################
#
# #Z. FizzBuzz
#
# Napisać program, który pobierze jako argument na wierszu poleceń liczbę, a
# następnie dla każdej liczby n od 1 do pobranej włącznie:
#
# - wypisze n na ekran
# - jeśli n jest podzielne przez 3 wypisze "Fizz"
# - jeśli n jest podzielne przez 5 wypisze "Buzz"
# - jeśli n jest podzielne przez 3 i 5 wypisze "FizzBuzz"

n=15
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print(i, "FizzBuzz")
    elif i%3==0:
        print(i, "Fizz")
    elif i%5==0:
        print(i, "Buzz")
    else:
        print(i, "error")
print("\n")

#sposob2#######################################

for i in range(1,n+1):
    fizzBuzz=[]
    if i%3==0:
        fizzBuzz.append("Fizz")
    if i%5==0:
        fizzBuzz.append("Buzz")
    if fizzBuzz:
        print(i,"".join(fizzBuzz))
    else:
        print(i, "error")
print("\n")

##############################################################

print("Ala ma kota")
Kot=["Ala","ma","kota"]
print(Kot)
print(" ".join(Kot))
print("?".join(Kot))
print("\n")

#################################################################
#
# # Z. Bottles of beer
#
# > 99 bottles of beer on the wall, 99 bottles of beer.
# > Take one down, pass it around, 98 bottles of beer on the wall...
#
# Jeśli 0:
#
# > No more bottles of beer on the wall, no more bottles of beer.
# > Go to the store and buy some more, 99 bottles of beer on the wall...

Beer=3
for i in range(Beer,-1,-1):
    if i==0:
        print(f"> No more bottles of beer on the wall, no more bottles of beer.\n> Go to the store and buy some more, {Beer} bottles of beer on the wall...")
    else:
        print(f"> {i} bottles of beer on the wall, {Beer} bottles of beer.\n> Take one down, pass it around, {i-1} bottles of beer on the wall...")
        print("\n")
print("\n")

####################################################################