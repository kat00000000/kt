import knapsack
import pytest

def test_capacity_init():
     assert knapsack.Knapsack(10).capacity_get() == 10

def test_capacity_init2():
     with pytest.raises(ValueError):
          assert knapsack.Knapsack("a").capacity_get()

def test_capacity_set1():
     test_knapsack = knapsack.Knapsack(10)
     test_knapsack.capacity_set(5)
     assert test_knapsack.capacity_get() == 5

def test_capacity_set2():
     with pytest.raises(ValueError):
          test_knapsack = knapsack.Knapsack(10)
          assert test_knapsack.capacity_set("a") 
          assert test_knapsack.capacity_get() == 10
