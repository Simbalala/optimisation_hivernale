import sys
from node import Node


class Graph():

    def __init__(self, nodes):
        self.node = {}
        for i in nodes:
            self.nodes[i] = {}

    def add_weighted_edges_from(self, list_edges):
        for e in list_edges:
            #e = (n1,n2,w)
            # If the edge was already there, just increase its number
            if e.n1 in self.nodes[e.n1]:
                self.nodes[e.n1][e.n2]["number"] += 1
            else:
                self.nodes[e.n1][e.n2] = {"weight": e[2], "number": 1}

            self.nodes[e[1]][e[0]] = self.nodes[e[0]][e[1]]

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for cout in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        self.pSol(dist)

    def find_odd_nodes(self):
        return [node for node in self.graph.nodes if len(self.graph[node]) % 2]
