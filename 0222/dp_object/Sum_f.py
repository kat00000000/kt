# coding : utf-8

import item_list_f
import knapsack_f

class Dp:
    def __init__(self):
        pass

    def dp_table_get(self,Item_number,knapsack_weight):
        if Item_number < len(self._dp_table) and 0 <= Item_number:
            if knapsack_weight < len(self._dp_table[Item_number]) and 0 <= knapsack_weight:
                return self._dp_table[Item_number][knapsack_weight]
            else:
                return 1
        else:
            return 1

    def dp_table_create(self):
        self._dp_table = [[0 for i in range(100010)] for j in range(110)]

    def dp_table_set(self,Item_number,knapsack_weight,value):
        if Item_number < len(self._dp_table) and 0 <= Item_number:
            if knapsack_weight < len(self._dp_table[Item_number]) and 0 <= knapsack_weight:
                self._dp_table[Item_number][knapsack_weight] = value
                return 0
            else:
                print("dp_table_setエラー")
                return 1
        else:
            print("dp_table_setエラー")
            return 1
    def maxSum_update(self,Item_list,Knapsack):
        item_list_len = Item_list.list_length()
        max_sum = 0

        for i in range(Knapsack.capacity_get() + 1):
            if max_sum < self.dp_table_get(item_list_len,i):
                max_sum = self.dp_table_get(item_list_len,i)
        return max_sum

    def dp_max(self,Item_list,Knapsack):
        item_number = Item_list.list_length()

        knapsack_weight = Knapsack.capacity_get()

        self.dp_table_create()

        for i in range(item_number):
            for j in range(knapsack_weight + 1):
                Item_list_weight = Item_list.list_get(i).weight_get()
                Item_list_value = Item_list.list_get(i).value_get()

                if Item_list_weight <= j:
                    dp_table_update_value = self.dp_table_get(i,(j - Item_list_weight)) + Item_list_value
                    if self.dp_table_get(i,j) < dp_table_update_value:
                        self.dp_table_set((i+1),j,dp_table_update_value)
                    else:
                        self.dp_table_set((i+1),j,self.dp_table_get(i,j))
                else:
                    self.dp_table_set((i+1),j,self.dp_table_get(i,j))

        return self.maxSum_update(Item_list,Knapsack)

if __name__ == "__main__":
    sum2 = Sum()
    sum2.dp_table_create()
    print(sum2.dp_table_set(100,10000,11))
    print(sum2.dp_table_get(100,10000))