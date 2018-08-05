# Wyszukuje najmniejszy element w tablicy i zwraca jego index
def find_smaller(arr):
    smallest = arr[0] # Przechowuje najmniejsza wartosc
    smallest_index = 0 # Indeks najmniejszej wartosci
    # Sprawdz wszystkie elementy tablicy
    for i in range(1, len(arr)):
        # Jesli mniejszy to zapisz
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index