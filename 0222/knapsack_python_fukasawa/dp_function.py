# coding : utf-8

import knapsack
import item

class Dp_function: 
    
    def _max(self, a, b):
        if a > b:
            return a
        else:
            return b
    
    def _dp_table_create(self, capacity, item):
        self._dp_table = [[0 for i in range(capacity + 1)]
        for j in range(item + 1)]

#    def _dp_table_set(self, item_count, weight, value):
#        self._dp_table[item_count][weight] = value

    def _dp_table_get(self, item_count, weight):
        return self._dp_table[item_count][weight]    
    
    def _dp_table_all(self):
        return self._dp_table

    def _dp_table_update(self, item_count, capacity, weight_table,value_table):
        for i in range(item_count):
            for j in range(capacity + 1):
                if weight_table[i] <= j:
                    self._dp_table[i + 1][j] = self._max(self._dp_table[i][j - weight_table[i]] + value_table[i], self._dp_table[i][j])
                else:
                    self._dp_table[i + 1][j] = self._dp_table[i][j]
 #               print(self._dp_table)
        return self. _dp_table

    def _maxvalue_update(self, _dp_table, item_count, capacity):
        for i in range(capacity):
            self._maxvalue = self._max(self. _dp_table[item_count][i], self._dp_table[item_count][i + 1])
        return self._maxvalue    
        
    def dp_max(self,item_count, capacity, value_table, weight_table):
        
        #knapsack1 = knapsack.Knapsack(0)
        #item1 = item.Item(0)

        #item_count = item1.item_count_get()
        #capacity = knapsack1.capacity_get()

        self._dp_table_create(capacity, item_count) 
       
        #value_table = item1.value_table_get()
        #weight_table = item1.weight_table_get()

#        print(value_table,weight_table)
        all_table = self._dp_table_update(item_count, capacity, weight_table, value_table)
        
        result = self._maxvalue_update(all_table, item_count, capacity) 

#       print(self._dp_table_all())
        return result

if __name__ == "__main__":  

    dp_function1 = Dp_function(0)

    dp_function1._dp_table_create(3,5)
    print(dp_function1._dp_table_get(0,0))
#    print(dp_function1._dp_table_all())
    print(dp_function1._max(2,1))
