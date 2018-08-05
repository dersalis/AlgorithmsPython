# Sortowanie szybkie
def quick_sort(numbers):
    # Jesli tablica ma mniej niz 2 elemnty to zwracamy nie sortujemy
    if len(numbers) < 2:
        return  numbers
    else:
        pivot = numbers[0] # Element osiowy
        # Elementy wieksze od osiowego
        greater = [i for i in numbers[1:] if i > pivot]
        # Elementy mniejsze od osiowego
        less = [i for i in numbers[1:] if i <= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
