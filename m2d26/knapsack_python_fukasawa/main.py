# coding : utf-8

import knapsack
import dp_function
import item

item1 = item.Item(0)
#print(item1)
knapsack1 = knapsack.Knapsack(0)

item1.item_count_set(int(input()))
knapsack1.capacity_set(int(input()))

_item_number = item1.item_count_get()
#print(type(_item_number))

item1.value_table_create(_item_number)
item1.weight_table_create(_item_number)

for i in range(_item_number):
    item1.value_table_set(int(input()), i)
    item1.weight_table_set(int(input()), i)
    
dp_function1 = dp_function.Dp_function()

print("MAX ", dp_function1.dp_max(_item_number, knapsack1.capacity_get(), item1.value_table_get(), item1.weight_table_get()))

#if __name__ == "__main__":
#
#    print(knapsack)
#    print(knapsack.Knapsack)
#    knapsack1 = knapsack.Knapsack(10)
#    print(knapsack1.capacity_get())
#    knapsack1.capacity_set(100000)
#    print(knapsack1.capacity_get())