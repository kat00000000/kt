# coding : utf-8

class Knapsack:
    #コンストラクタ
    def __init__(self,capacity): #selfは自分のクラスを渡すという意味
        self._capacity = capacity
    #クラスメソッド
    def capacity_check(self):
        print(self._capacity)
    def capacity_get(self):
        return self._capacity
    def capacity_set(self,input):
        self._capacity = input
        
if __name__ == "__main__":
    
    #create Class instance
    knapsack1 = Knapsack(100)
    knapsack2 = Knapsack(100000)
    
    knapsack1.capacity_set(10)
    print(knapsack1.capacity_get())



