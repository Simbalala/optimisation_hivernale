from graph import Graph
#        5      3 
#   0 ----- 1 ----- 2
#   |       |       |
#  2|      6|      7|
#   |       |       |
#   3 ----- 4 ----- 5
#       1       2

def theorical_exemple():
    g = Graph(6)
    g.graph = [[0, 5, 0, 2, 0, 0],
        [5, 0, 3, 0, 6, 0],
        [0, 3, 0, 0, 7, 0],
        [2, 0, 0, 0, 1, 0],
        [0, 6, 0, 0, 0, 2],
        [0, 0, 7, 0, 2, 0]
        ]
    g.dijkstra(0)


def main():
    G = theorical_exemple()

if __name__ == "__main__":
    main()
