from collections import deque

# Sprawdz osobe
def person_is_seller(name):
    # Jesli pierwsza litera imienia to m oznacze ze sprzedaje - taki myk
    return name[0] == 'm'

# Wyszukiwanie
def search(name):
    search_queue = deque()
    search_queue += graph[name] # Dodaj powiazania szukanej osoby
    searched = [] # Tablica sprawdzonych osob - aby ponownie nie przeszukiwac
    # Sprawdzaj dopuki na stosie sa osoby
    while search_queue:
        person = search_queue.popleft()
        # Sprawdz czy osoba byla sprawdzana
        if not person in searched:
            print(person)
            # Sprawdz czy jest sprzedawca
            if person_is_seller(person):
                print(f"{person} sprzedaje mango!")
                return True
            else:
                # Dodaj do listy wyszukiwania powiazane osoby
                search_queue += graph[person]
                searched.append(person) # Dodaje do sprawdzonych
    return False


# Powiazania miedy osobami w postaci grafu
graph = {}
graph["ty"] = ["alicja", "bartek", "cecylia"]
graph["bartek"] = ["janusz", "marta"]
graph["alicja"] = ["marta"]
graph["cecylia"] = ["tamara", "jarek"]
graph["janusz"] = []
graph["marta"] = []
graph["tamara"] = []
graph["jarek"] = []

search("ty")