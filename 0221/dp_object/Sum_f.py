# coding : utf-8

import item_list_f
#import item_f
import knapsack_f

class Sum:
    def __init__(self):
        pass

    def dp_table_get(self,Item_number,knapsack_weight):
        return self._dp_table[Item_number][knapsack_weight]

    def dp_table_create(self):
        self._dp_table = [[0 for i in range(100010)] for j in range(100)]

    def dp_table_set(self,Item_number,knapsack_weight,value):
        self._dp_table[Item_number][knapsack_weight] = value
        return 0

    def maxSum_update(self,Item_list,Knapsack):
        #Knapsack = knapsack_f.Knapsack()
       # Item_list = item_list_f.Item_list()
        item_list_len = Item_list.item_length()
        max_sum = 0

        for i in range(Knapsack.capacity_get()):
            if max_sum < self.dp_table_get(item_list_len,i):
                max_sum = self.dp_table_get(item_list_len,i)
        return max_sum

    def dp_max(self,Item_list,Knapsack):
        #Item_list = item_list_f.Item_list()
        item_number = Item_list.item_length()

       # Knapsack = knapsack_f.Knapsack()
        knapsack_weight = Knapsack.capacity_get()

        self.dp_table_create()

        for i in range(item_number):
            for j in range(knapsack_weight):
                Item_list_weight = Item_list.item_list_get(i).weight_get()
                Item_list_value = Item_list.item_list_get(i).value_get()

                if Item_list_weight <= j:
                    dp_table_update_value = self.dp_table_get(i,(j - Item_list_weight)) + Item_list_value
                    if self.dp_table_get(i,j) < dp_table_update_value:
                        self.dp_table_set((i+1),j,dp_table_update_value)
                    elif dp_table_update_value <= self.dp_table_get(i,j):
                        self.dp_table_set((i+1),j,self.dp_table_get(i,j))
                    else:
                        pass
                elif j < Item_list_value:
                     self.dp_table_set((i+1),j,self.dp_table_get(i,j))
                else:
                    pass

        return self.maxSum_update(Item_list,Knapsack)
    