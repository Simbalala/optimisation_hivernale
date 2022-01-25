from graph import Graph
from chinese_postman import *
import osmnx as ox
import argparse


def getopt():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all',
                        help='Start project on 19 arrondicement of Monreal',
                        action='store_true')
    parser.add_argument('-c', '--city',
                        help='Start project on sector pass in params')

    return parser.parse_args()

def all_monreal():
    city = ['Anjou, Montréal, QC, Canada']
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

def set_geoloc(geoloc):
    g_osmnx = ox.graph_from_place(geoloc, network_type='drive')
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


def main():
    args = getopt()
    if args.all:
        all_monreal()
    if args.city:
        set_geoloc(args.city)
    
   





if __name__ == "__main__":
    main()
