# -*- coding: utf8 -*-
from collections import deque

def find_way(cityFrom, cityTo):
    way_queue = deque()
    # Dodaj wszystkie polaczenia z miasta poczatkowego
    way_queue += way_graph[cityFrom]
    # Sprawdz wszystkie miasta
    while way_queue:
        city = way_queue.popleft()
        print(city)
        # Jesli jest polaczenie
        if city == cityTo:
            print(f"Jest połączenie z {cityTo}")
            #return True
        else:
            if city in way_graph:
                find_way(city, cityTo)
    #return False

# Opis polaczen drogowych
way_graph = {}
way_graph["szczecin"] = ["piła"]
way_graph["piła"] = ["gorzów", "poznań", "bydgoszcz"]
way_graph["gorzów"] = ["kostrzyn nad odrą", "zielona góra"]
way_graph["poznań"] = ["wrocław", "warszawa"]
way_graph["zielona góra"] = ["szklarska poręba"]
way_graph["wrocław"] = ["karpacz", "kraków", "katowice"]
way_graph["warszawa"] = ["radom", "mińsk"]
way_graph["kraków"] = ["zakopane"]
way_graph["bydgoszcz"] = ["warszawa"]

find_way("szczecin", "warszawa")