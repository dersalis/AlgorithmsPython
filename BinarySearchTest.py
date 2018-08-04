from BinarySearch import binary_search

print("*** WYSZUKIWANIE BINARNE ***")
# Poczatek zakresu
lNumber = int(input("Poczatek zakresu: "))
# Koniec zakresu
hNumber = int(input("Koniec zakresu: "))
# Poczatek zakresu musi byc wiekszy od konca
if lNumber < hNumber:
    sNumber = int(input("Szukana liczba: "))
    # Testowe dane
    test_data = list(range(lNumber, hNumber, 1))
    # Wyszukaj i zwroc pozycje
    print(binary_search(test_data, sNumber))
else:
    print("Poczatek zakresu musi byc wiekszy od konca!")
