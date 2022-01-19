from numpy import inf, argmin

def dijkstra(graph, source, target):
    """
    """
    visited = {node : False for node in graph.nodes}
    unvisited = [node for node in graph.nodes]
    distance = {node : inf for node in graph.nodes}
    distance[source] = 0
    previous = {node : None for node in graph.nodes}
    while unvisited:
        index = argmin([distance[node] for node in unvisited])
        current = unvisited.pop(index)
        for neighbor in graph[current] :
            if not visited[neighbor] :
                if distance[current] + graph[current][neighbor].weight <= distance[neighbor] :
                    distance[neighbor] = distance[current] + graph[current][neighbor].weight
                    previous[neighbor] = current
        visited[current] = True

    path = [target]
    while path[0] != source :
        path = [previous[path[0]]] + path

    return path, distance[target] 


def chinese_postman(G, start):
    odd = G.odd_nodes()
    pairs = G.node_pairings(odd)

    min_sum = inf
    final_dijkstra = []
    for p in pairs:
        d = [dijkstra(G, i, j) for (i,j) in p]
        s = sum([i[1] for i in d])                 
        if s < min_sum :
            min_sum = s
            final_dijkstra = d

    G.add_weighted_edges_from([(d[0][i], d[0][i+1], None) for d in final_dijkstra for i in range(len(d[0])-1)])
    cycle = [start]
    len_edges = len(G.get_all_edges())

    while len(cycle) != len_edges:

        edges = [e for e in G.get_all_edges() if e[2].visit > 0]

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

            for neighbor in G[current]:
                if G[current][neighbor].visit > 0:
                    G[current][neighbor].visit -= 1
                    sub_path.append(neighbor)
                    flag = True
                    break
        
        cycle = cycle[:sub_index] + sub_path[1:] + cycle[sub_index:]

    return cycle