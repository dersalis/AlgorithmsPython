import math

def binary_search(list, item):
    low = 0 # Pozycja pierwszego elementu
    high = len(list) - 1 # Pozycja ostatniego elementu
    while low <= high:
        # Oblicz pozycję elementu środkowego
        mid = int((low + high) / 2)
        # Srodkowy element
        result = list[mid]
        # Jeśli znaleziono
        if result == item:
            return result
        if result > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# Testowe dane
test_data = list(range(1, 1024, 2))
# Wyszukaj i zwróć pozycję
print(binary_search(test_data, 45))
