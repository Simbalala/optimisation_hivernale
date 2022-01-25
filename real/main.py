from graph import Graph
from chinese_postman import *
import osmnx as ox
import argparse

def main():
    args = parse_args()



    g_osmnx = ox.graph_from_place('Anjou, Montréal, QC, Canada', network_type='drive')
    G = Graph(g_osmnx.nodes)
    G.add_edges(g_osmnx.edges(data='length'))
    ttk = sum(node[2].weight for node in G.all_edges())
    tpk = sum(node[2].weight * node[2].visit for node in G.all_edges())

    l = list(g_osmnx.nodes.items())
    cycle = chinese_postman(G, l[0][0])
   
    print("Distance total theorique in km: ", ttk)
    print("Distance total parcourue in km: ", tpk)
    print(f"Ratio: {(ttk / tpk)* 100}%")
    print("\nResult route path:", cycle)




if __name__ == "__main__":
    main()
