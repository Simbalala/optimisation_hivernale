import sys
from node import Node

class Graph():

    def __init__(self, lnode):
        self.nodes = {}
        for n in lnode :
            self.nodes[n] = {}
    
    def __getitem__(self, key):
        return self.nodes[key]
    
    def add_weighted_edges_from(self, edges):
        for edge in edges :
            if edge[1] in self.nodes[edge[0]] :
                self.nodes[edge[0]][edge[1]].visit += 1
            else :
                self.nodes[edge[0]][edge[1]] = Node(edge[2], 1)
            self.nodes[edge[1]][edge[0]] = self.nodes[edge[0]][edge[1]]
    
    def odd_nodes(self):
        return [node for node in self.nodes if len(self.nodes[node]) % 2] 

    def node_pairings(self, nodes):
        if len(nodes) == 0:
            return []
        final = []

        for i in range(1, len(nodes)):
            perm = self.node_pairings(nodes[1:i] + nodes[i+1:])
            for p in perm :
                final.append([(nodes[0], nodes[i])]+p)
            if len(perm) == 0:
                final.append([(nodes[0], nodes[i])])
        return final
    
    def get_all_edges(self) :
        result = []
        for n1 in self.nodes :
            for n2 in self.nodes[n1] :
                if (n2, n1, self.nodes[n1][n2]) not in result :
                    result.append((n1, n2, self.nodes[n1][n2]))
        return result
