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
    citys = ['Ahuntsic-Cartierville, Montréal, QC, Canada',
            'Anjou, Montréal, QC, Canada']
            # 'Côte-des-Neiges–Notre-Dame-de, Montréal, QC, Canada',
            # 'Lachine, Montréal, QC, Canada',
            # 'LaSalle, Montréal, QC, Canada',
            # 'Le Plateau-Mont-Royal, Montréal, QC, Canada',
            # 'Le Sud-Ouest, Montréal, QC, Canada',
            # 'L\'Île-Bizard–Sainte-Geneviève, Montréal, QC, Canada',
            # 'Mercier–Hochelaga-Maisonneuve, Montréal, QC, Canada',
            # 'Montréal-Nord, Montréal, QC, Canada',
            # 'Outremont, Montréal, QC, Canada',
            # 'Pierrefonds-Roxboro, Montréal, QC, Canada',
            # 'Rivière-des-Prairies—Pointe-aux-Trembles—Montréal-Est, Montréal, QC, Canada',
            # 'Rosemont–La Petite-Patrie, Montréal, QC, Canada',
            # 'Saint-Laurent, Montréal, QC, Canada',
            # 'Saint-Léonard, Montréal, QC, Canada',
            # 'Verdun, Montréal, QC, Canada',
            # 'Villeray–Saint-Michel–Parc-Extension, Montréal, QC, Canada',
            # 'Ville-Marie, Montréal, QC, Canada']
    result = {}
    for city in citys:
        g_osmnx = ox.graph_from_place('city', network_type='drive')
        G = Graph(g_osmnx.nodes)
        G.add_edges(g_osmnx.edges(data='length'))
        ttk = sum(node[2].weight for node in G.all_edges())
        tpk = sum(node[2].weight * node[2].visit for node in G.all_edges())

        l = list(g_osmnx.nodes.items())
        cycle = chinese_postman(G, l[0][0])
        result[city] = {'distance_theo': ttk, 'distance_reel': tpk, 'ratio': (ttk / tpk)* 100, 'path': cycle}
    
    for key, value in result.items():
        print(f"{key}: ")
        print("    Distance total theorique in km: ", value['distance_theo'])
        print("    Distance total parcourue in km: ",  value['distance_reel'])
        print(f"    Ratio: {value['ratio']}%")
        print("    Result route path:", value['path'])
        print("")

def set_geoloc(geoloc):
    g_osmnx = ox.graph_from_place(geoloc, network_type='drive')
    G = Graph(g_osmnx.nodes)
    G.add_edges(g_osmnx.edges(data='length'))
    ttk = sum(node[2].weight for node in G.all_edges())
    tpk = sum(node[2].weight * node[2].visit for node in G.all_edges())

    l = list(g_osmnx.nodes.items())
    cycle = chinese_postman(G, l[0][0])
    print(f"{geoloc}: ")
    print("    Distance total theorique in km: ", ttk)
    print("    Distance total parcourue in km: ", tpk)
    print(f"    Ratio: {(ttk / tpk)* 100}%")
    print("    Result route path:", cycle)


def main():
    args = getopt()
    if args.all:
        all_monreal()
    if args.city:
        set_geoloc(args.city)

if __name__ == "__main__":
    main()
