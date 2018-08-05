# Wyszukuje najwiekszy element w tablicy
def find_biggest(arr):
    biggest = arr[0] # Najwiekszy element w tablicy
    biggest_index = 0 # Indeks najwiekszego elementu w tablicy
    # Sprawdz wszystkie elmenty tablicy
    for i in range(1, len(arr)):
        # Jesli wiekszy to zapisz
        if arr[i] > biggest:
            biggest = arr[i]
            biggest_index = i
    return biggest_index