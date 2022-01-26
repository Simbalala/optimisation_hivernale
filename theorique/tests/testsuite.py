import pathlib, sys
from traceback import print_stack
path = str(pathlib.Path(__file__).parent.absolute().parent) + "/"
sys.path.append(path)

from graph import Graph
from chinese_postman import *
from termcolor import colored
import unittest

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

# Test 3 :
#       5       3
#   0 ----- 1 ----- 2
#   |               |
#  2|              7|
#   |               |
#   3 ----- 4 ----- 5
#       1       2

def theorical_exemple_4():
    g = Graph(range(0,6))
    g.add_edges([(0, 1, 5), (0, 3, 2),
                (1, 2, 3),
                (2, 5, 7),
                (3, 4, 1),
                (4, 5, 2)])
    return g


class Test_trajet(unittest.TestCase):

    def test_1(self):
        G_1 = theorical_exemple_1()
        print_1 = chinese_postman(G_1, 0)
        self.assertEqual(print_1, [0, 1, 2, 5, 4, 1, 4, 3, 0])

    def test_2(self):
        G_2 = theorical_exemple_2()
        print_2 = chinese_postman(G_2, 0)
        self.assertEqual(print_2, [0, 1, 2, 5, 4, 1, 0, 3, 4, 7, 6, 3, 0])

    def test_3(self):
        G_3 = theorical_exemple_3()
        print_3 = chinese_postman(G_3, 0)
        self.assertEqual(print_3, [0, 1, 0, 3, 4, 5, 2, 1, 7, 6, 0])

    def test_Eulerien(self):
        G_4 = theorical_exemple_4()
        print_4 = chinese_postman(G_4, 0)
        self.assertEqual(print_4, [0, 1, 2, 5, 4, 3, 0])

if __name__ == '__main__':
    unittest.main()
