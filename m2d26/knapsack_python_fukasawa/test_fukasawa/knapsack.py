# coding : utf-8
import pytest

class Knapsack: #__init__   コンストラクタ、オブジェクトが生成されるときに実行されるメソッド（関数）
    def __init__(self, capacity):    #変数。自分を渡している
        if (isinstance(capacity, int)):
            self._capacity = capacity   #privateの変数は_を付ける
        else:
            raise ValueError("error!")
            #self._capacity = "error"
    #def capacity_check(self):   #メソッドはdef
    #    print (self._capacity)
    def capacity_get(self):
        return self._capacity
    def capacity_set(self,input):
        if (isinstance(input, int)):
            self._capacity = input
        else:
            raise ValueError("error!")

if __name__ == "__main__":  
    #クラスのインスタンス化(実体化)
    knapsack1 = Knapsack(100)
    print (knapsack1.capacity_get())
    knapsack1.capacity_set(10)
    print (knapsack1.capacity_get())

