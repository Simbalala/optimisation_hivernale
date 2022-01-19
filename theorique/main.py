from graph import Graph
from chinese_postman import *

#        5      3 
#   0 ----- 1 ----- 2
#   |       |       |
#  2|      6|      7|
#   |       |       |
#   3 ----- 4 ----- 5
#       1       2

def theorical_exemple():
    g = Graph(range(0,6))
    g.add_weighted_edges_from([(0, 1, 5), (0, 3, 2),
                                (1, 2, 3), (1, 4, 6),
                                (2, 5, 7),
                                (3, 4, 1),
                                (4, 5, 2)])
    print(chinese_postman(g, 0))
    return g


def main():
    G = theorical_exemple()
    # print(G.edges)

if __name__ == "__main__":
    main()
