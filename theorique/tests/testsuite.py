import pathlib, sys
path = str(pathlib.Path(__file__).parent.absolute().parent) + "/"
sys.path.append(path)

from graph import Graph
from chinese_postman import *

# Test 1 :

#        5      3 
#   0 ----- 1 ----- 2
#   |       |       |
#  2|      6|      7|
#   |       |       |
#   3 ----- 4 ----- 5
#       1       2

def theorical_exemple_1():
    g = Graph(range(0,6))
    g.add_edges([(0, 1, 5), (0, 3, 2),
                (1, 2, 3), (1, 4, 6),
                (2, 5, 7),
                (3, 4, 1),
                (4, 5, 2)])
    return g

# Test 2 :

#        5      3 
#   0 ----- 1 ----- 2
#   |       |       |
#  2|      6|      7|
#   |       |       |
#   3 ----- 4 ----- 5
#   |   1   |   2
#   |       |
#  2|      6|
#   |       |
#   6 ----- 7
#       1 

def theorical_exemple_2():
    g = Graph(range(0,8))
    g.add_edges([(0, 1, 5), (0, 3, 2),
                (1, 2, 3), (1, 4, 6),
                (2, 5, 7),
                (3, 4, 1), (3, 6, 2),
                (4, 5, 2), (4, 7, 6),
                (6, 7, 1)])
    return g


def main():
    print("\nFirst Test : ")
    G_1 = theorical_exemple_1()
    print(chinese_postman(G_1, 0))

    print("\nSecond Test : ")
    G_2 = theorical_exemple_2()
    print(chinese_postman(G_2, 0))


if __name__ == "__main__":
    main()
