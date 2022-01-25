from graph import Graph
from chinese_postman import *
import osmnx as ox

def main():
    g_osmnx = ox.graph_from_place('Anjou, Montréal, QC, Canada', network_type='drive')
    G = Graph(g_osmnx.nodes)
    G.add_edges(g_osmnx.edges(data='length'))

    l = list(g_osmnx.nodes.items())
    cycle = chinese_postman(G, l[0][0])

    print("\nResult path:", cycle)

if __name__ == "__main__":
    main()
