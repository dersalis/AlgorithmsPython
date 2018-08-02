
def binary_search(list, item):
    low = 0 # Pozycja pierwszego elementu
    high = len(list) - 1 # Pozycja ostatniego elementu
    steps = 0
    while low <= high:
        # Zwiększ licznik
        steps += 1
        # Oblicz pozycję elementu środkowego
        mid = int((low + high) / 2)
        # Srodkowy element
        result = list[mid]
        # Jeśli znaleziono
        if result == item:
            print(f"Liczba kroków: ", steps)
            return result
        if result > item:
            high = mid - 1
        else:
            low = mid + 1

    return None
