import pathlib, sys
path = str(pathlib.Path(__file__).parent.absolute().parent) + "/"
sys.path.append(path)

from graph import Graph
from chinese_postman import *
from termcolor import colored

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

# Test 3 :

#       1
#   6 ---- 7
#   |       |
#  2|      3|
#   |   5   |   3 
#   0 ----- 1 ----- 2
#   |               |
#  2|              7|
#   |               |
#   3 ----- 4 ----- 5
#       1       2

def theorical_exemple_3():
    g = Graph(range(0,9))
    g.add_edges([(0, 1, 5), (0, 3, 2),
                (1, 2, 3),
                (2, 5, 7),
                (3, 4, 1),
                (4, 5, 2),
                (0,6,2), (1,7,3),
                (6,7,1)])
    return g

# Test 4 :

#       1
#   6 ---- 7
#   |       |
#  2|      3|
#   |   5   |   3 
#   0 ----- 1 ----- 2
#   |               |
#  2|              7|
#   |               |
#   3 ----- 4 ----- 5
#       1       2

def theorical_exemple_4():
    g = Graph(range(0,9))
    g.add_edges([(0, 1, 5), (0, 3, 2),
                (1, 2, 3),
                (2, 5, 7),
                (3, 4, 1),
                (4, 5, 2),
                (0,6,2), (1,7,3),
                (6,7,1)])
    return g

def ratio(G):
    ttk = sum(node[2].weight for node in G.all_edges())
    tpk = sum(node[2].weight * node[2].visit for node in G.all_edges())
    print(tpk)
    print(ttk)
    return (ttk/tpk)*100 + 100


def main():
    print("\nFirst Test : ")
    G_1 = theorical_exemple_1()
    ok = print(chinese_postman(G_1, 0))
    if assert ok == [0, 1, 2, 5, 4, 1, 4, 3, 0]:
        print(f"[{colored('KO', 'red')}]", testcase["name"])
    print(f"[{colored('OK', 'green')}]", testcase["name"])

    print("\nSecond Test : ")
    G_2 = theorical_exemple_2()
    print(chinese_postman(G_2, 0))
    print(f"[{colored('KO', 'red')}]", testcase["name"])
    print(f"[{colored('OK', 'green')}]", testcase["name"])

    print("\nThird Test : ")
    G_3 = theorical_exemple_3()
    print(chinese_postman(G_3, 0))
    print(f"[{colored('KO', 'red')}]", testcase["name"])
    print(f"[{colored('OK', 'green')}]", testcase["name"])

    print("\nFourth Test : ")
    G_4 = theorical_exemple_4()
    print(chinese_postman(G_4, 0))
    print(f"[{colored('KO', 'red')}]", testcase["name"])
    print(f"[{colored('OK', 'green')}]", testcase["name"])


if __name__ == "__main__":
    main()
