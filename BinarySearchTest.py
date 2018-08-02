from BinarySearch import binary_search

print("*** WYSZUKIWANIE BINARNE ***")
# Początek zakresu
lNumber = int(input("Początek zakresu: "))
# Koniec zakresu
hNumber = int(input("Koniec zakresu: "))
# Początek zakresu musi być większy od końca
if lNumber < hNumber:
    sNumber = int(input("Szukana liczba: "))
    # Testowe dane
    test_data = list(range(lNumber, hNumber, 1))
    # Wyszukaj i zwróć pozycję
    print(binary_search(test_data, sNumber))
else:
    print("Początek zakresu musi być większy od końca!")
