def foo(a, b, c, *reszta):
    return len(reszta)

def bar(a, b, c, magiczna_liczba = liczba):
    if opcje.get(liczba) == 7:
        return True
    else:
        return False



if foo(1,2,3,4) == 1:
    print ("Dobrze.")
if foo(1,2,3,4,5) == 2:
    print ("Lepiej.")
if bar(1,2,3,magiczna_liczba = 6) == False:
    print ("Bardzo dobrze.")
if bar(1,2,3,magiczna_liczba = 7) == True:
    print ("Doskonale!")