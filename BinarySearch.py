
def binary_search(items_list, item):
    low_index = 0  # Poczatkowy indeks przeszukiwania
    high_index = len(items_list) - 1  # Koncowy indeks przeszukiwania
    steeps = 1  # Licznik krokow
    # Szukaj dopuki indeksy sa rozne
    while low_index <= high_index:
        # Indeks srodkowego elementu
        mid_index = int(low_index + high_index) / 2
        # Wskaz wartosc przy srodkowym indeksie
        curr_item = items_list[mid_index]
        # Jesli liczby rowne to zwroc
        if item == curr_item:
            print "Liczba krokow: ", steeps
            return mid_index
        # Jesli rozne to zmien zakres przeszukiwania
        if item < curr_item:
            high_index = curr_item - 1
        else:
            low_index = curr_item + 1
        steeps += 1  # Zwieksz licznik
    # Jesli nie znaleziono
    return None
