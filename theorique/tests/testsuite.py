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
#   |   1   |   2   |
#   |       |       |
#  2|      6|      7|
#   |       |       |
#   6 ----- 7 ----- 8
#       1       2

def theorical_exemple_2():
    g = Graph(range(0,6))
    g.add_edges([(0, 1, 5), (0, 3, 2),
                (1, 2, 3), (1, 4, 6),
                (2, 5, 7),
                (3, 4, 1), (3, 6, 2),
                (4, 5, 2), (4, 7, 6),
                (5, 8, 7),
                (6, 7, 1),
                (7, 8, 2)])
    return g


# Test 3 :

#        5      3       5
#   0 ----- 1 ----- 2 ----- 9
#   |       |       |       |
#  2|      6|      7|      6|
#   |       |       |       |
#   3 ----- 4 ----- 5 ----- 10
#   |   1   |   2   |   3
#   |       |       |
#  2|      6|      7|
#   |       |       |
#   6 ----- 7 ----- 8
#       1       2

def theorical_exemple_3():
    g = Graph(range(0,6))
    g.add_edges([(0, 1, 5), (0, 3, 2),
                (1, 2, 3), (1, 4, 6),
                (2, 5, 7), (2, 9, 5),
                (3, 4, 1), (3, 6, 2),
                (4, 5, 2), (4, 7, 6),
                (5, 8, 7), (5, 10, 3),
                (6, 7, 1),
                (7, 8, 2),
                (9, 10, 6)])
    return g


def main():
    print("\nFirst Test : \n")
    G_1 = theorical_exemple_1()
    print(chinese_postman(G_1, 0))

    print("\nSecond Test : \n")
    G_2 = theorical_exemple_2()
    print(chinese_postman(G_2, 0))

    print("\nThird Test : \n")
    G_3 = theorical_exemple_3()
    print(chinese_postman(G_3, 0))


if __name__ == "__main__":
    main()
