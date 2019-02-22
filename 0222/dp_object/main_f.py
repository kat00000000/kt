#coding : utf-8
import knapsack_f
import item_f
import item_list_f
import Sum_f

if __name__ == "__main__":
   knapsack = knapsack_f.Knapsack()
   item_list = item_list_f.Item_list()
   Sum = Sum_f.Sum()
   
   item_number = int(input())
   knapsack_weight = int(input())

   knapsack.capacity_set(knapsack_weight)
   item_list.list_Create(item_number)

   item_number = item_list.item_length()
   
   for i in range(item_number):
       input_weight,input_value = int(input()),int(input())
       item = item_f.Item()
       item.value_set(input_value)
       item.weight_set(input_weight)

       item_list.item_list_set(item,i)

   max_sum = Sum.dp_max(item_list,knapsack)
   print("最大値は",max_sum)

   pass