def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # Przegląda każdy węzeł po kolei.
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            „lowest_cost = cost # …ustaw go jako nowy najtańszy węzeł.
            lowest_cost_node = node
        return lowest_cost_node

node = find_lowest_cost_node(costs) # Znajduje najtańszy węzeł, który nie został jeszcze przetworzony.
while node is not None: # Jeśli wszystkie węzły zostały przetworzone, następuje zakończenie pętli.
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # Przegląda wszystkich sąsiadów danego węzła.
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # Jeśli dotarcie do tego sąsiada jest tańsze drogą przez ten węzeł…
            costs[n] = new_cost #… zaktualizuj koszt tego węzła.
            parents[n] = node # Węzeł ten staje się nowym rodzicem tego sąsiada.
    processed.append(node) # Oznaczenie węzła jako przetworzony.
    node = find_lowest_cost_node(costs)

graph = {}
graph["a"] = {}
graph["a"]["meta"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["meta"] = 5
graph["meta"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["meta"] = None

processed = []