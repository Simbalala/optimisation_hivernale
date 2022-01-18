import osmnx as ox

def main():
    G = ox.graph_from_place('Montréal, Canada')
    ox.plot_graph(G)

if __name__ == "__main__":
    main()
