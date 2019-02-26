#import knapsack

import sys
sys.path.append('/m2d26/knapsack_python_fukasawa')
import knapsack

def test_capacity_get():

     assert  knapsack.Knapsack(10).capacity_get() == 10

def test_add_01():
    pass