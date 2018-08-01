import math

def printRange(srange):
    for r in srange:
        print(r + ', ')


# Podaj liczbę początkową zakresu
fNumber = int(input("Podaj pierwszą liczbę zakresu: "))
# Podaj liczbę końcową zakresu
lNumber = int(input("Podaj ostatnią liczbę zakresu: "))
# Liczba końcowa musi być większa od początkowej
if lNumber <= fNumber:
    print("Ostatnia liczba zakresu musi być większa od pierwszej!")
else:
    # Licznik
    count = 1
    # Zakres
    #sRange = list(range(fNumber, lNumber))
    # Podaj szukaną liczbę
    sNumber = int(input("Podaj szukaną liczbę: "))
    # Szukana liczba musi należeć do zakresu
    if sNumber < fNumber or sNumber > lNumber:
        print("Liczba nie należy do zakresu!")
    else:
        # Jeśli liczba należy do zakresu
        cNumber = fNumber
        # Liczby
        #print(sRange)
        while 1:
            sRange = list(range(fNumber, lNumber + 1))
            print(f"{count}: {sRange}\n")
            count += 1
            cNumber = math.ceil((lNumber - fNumber) / 2) + fNumber
            if cNumber == sNumber:
                print(f"*** Znaleziono liczbę: {sNumber} ***")
                break
            else:
                if cNumber < sNumber:
                    fNumber = cNumber
                else:
                    lNumber = cNumber
