#coding : utf-8
import knapsack_f
import item_f
import item_list_f
import Sum_f

if __name__ == "__main__":

   knapsack = knapsack_f.Knapsack()
   item_list = item_list_f.Item_list()
   Sum = Sum_f.Dp()
   
   input_list_max = int(input())
   input_capacity = int(input())

   knapsack.capacity_set(input_capacity)
   item_list.list_Create(input_list_max)

   input_list_max = item_list.list_length()
   
   for i in range(input_list_max):
       input_weight,input_value = int(input()),int(input())
       item = item_f.Item()
       item.value_set(input_value)
       item.weight_set(input_weight)

       item_list.list_set(item,i)

   max_sum = Sum.dp_max(item_list,knapsack)
   print(max_sum)

   pass