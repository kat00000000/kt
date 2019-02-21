# coding : utf-8

class Sum:
    def __init__(self):
        self.dp_table = [[0 for i in range(100010)] for j in range(100)]
        self.maxSum = 0
    def dp_table_get(self,Item_number,knapsack_weight):
        return self.dp_table[Item_number][knapsack_weight]
    def dp_table_set(self,Item_number,knapsack_weight,value):
        self.dp_table[Item_number][knapsack_weight] = value
        return 0
    def dp_max(self):
        pass
    def maxSum_updata(self):
        pass