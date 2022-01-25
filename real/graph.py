import sys
from node import Node

class Graph():

    def __init__(self, nodes):
        self.v = len(nodes)
        self.edges = {}
        for node in nodes:
            self.edges[node] = {}
        self.visited = []
        
    def __getitem__(self, key):
        return self.edges[key]
    
    def add_edges(self, edges):
        for edge in edges:
            if edge[1] in self.edges[edge[0]]:
                self.edges[edge[0]][edge[1]].visit += 1
            else:
                self.edges[edge[0]][edge[1]] = Node(edge[2], 1)
            self.edges[edge[1]][edge[0]] = self.edges[edge[0]][edge[1]]
        
    
    def odd_nodes(self):
        return [node for node in self.edges if len(self.edges[node]) % 2]


    def node_pairings(self, nodes):
        if nodes == 0:
            return []
        final = []

        for i in range(1, len(nodes)):
            perm = self.node_pairings(nodes[1:i] + nodes[i+1:])
            for p in perm :
                final.append([(nodes[0], nodes[i])]+p)
            if len(perm) == 0:
                final.append([(nodes[0], nodes[i])])
        return final
    
    def all_edges(self) :
        result = []
        for n1 in self.edges:
            for n2 in self.edges[n1]:
                if (n2, n1, self.edges[n1][n2]) not in result :
                    result.append((n1, n2, self.edges[n1][n2]))
        return result
