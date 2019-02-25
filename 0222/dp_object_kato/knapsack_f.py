# coding : utf-8

class Knapsack:
    #コンストラクタ
    def __init__(self): #selfは自分のクラスを渡すという意味
        pass

    #クラスメソッド
    def capacity_get(self):
        return self._capacity

    def capacity_set(self,input_capacity):
        if 1 <= input_capacity and input_capacity <= 100000:        
            self._capacity = input_capacity
            return True
        else:
            return False
        
if __name__ == "__main__":
    
    #create Class instance
    knapsack1 = Knapsack()
    knapsack2 = Knapsack()
    
    knapsack1.capacity_set(10)
    print(knapsack1.capacity_get())



