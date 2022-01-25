from queue import Queue
from graph import Graph
from node import *

def dijkstra(graph, start, target):
    D = {v:float('inf') for v in range(graph.v)}
    D[start] = 0
    pq = Queue()
    pq.put((0, start))
    prev = {node : None for node in range(graph.v)}

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)
        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != None:
                distance = graph.edges[current_vertex][neighbor].weight
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
                        prev[neighbor] = current_vertex

    path = [target]
    while path[0] != start :
        path = [prev[path[0]]] + path
    return path, D[target]

def chinese_postman(G, start):
    
    pairs  = [[]]
    min_sum = float('inf')
    final_dijkstra = []
    for p in pairs:
        d = [dijkstra(G, i, j) for (i,j) in p]
        s = sum([i[1] for i in d])                 
        if s < min_sum :
            min_sum = s
            final_dijkstra = d

    G.add_edges([(d[0][i], d[0][i+1], None) for d in final_dijkstra for i in range(len(d[0])-1)])
    cycle = [start]
    len_edges = len(G.all_edges())

    while len(cycle) != len_edges:
        edges = [e for e in G.all_edges() if e[2].visit > 0]
        sub_path = None
        for e in edges :
            if e[0] in cycle :
                sub_path = [e[0]]
                break
            elif e[1] in cycle :
                sub_path = [e[1]]
                break
        
        if sub_path == None :
            break

        sub_index = cycle.index(sub_path[0]) + 1
        flag = True
        while flag:
            flag = False
            current = sub_path[-1]
            for i in G[current]:
                if G[current][i].visit > 0:
                    G[current][i].visit -= 1
                    sub_path.append(i)
                    flag = True
                    break
       
        cycle = cycle[:sub_index] + sub_path[1:] + cycle[sub_index:]
    return cycle