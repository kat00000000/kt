#coding : utf-8
import knapsack_f
import item_f
import item_list_f
import Sum_f
import sys

if __name__ == "__main__":

   knapsack = knapsack_f.Knapsack()
   item_list = item_list_f.Item_list()
   Sum = Sum_f.Dp()
   
   input_list_max = int(input())
   input_capacity = int(input())

   capacity_check = knapsack.capacity_set(input_capacity)
   if capacity_check == False:
      print("ナップサックの容量エラー")
      sys.exit()

   list_max_check = item_list.list_create(input_list_max)
   if list_max_check == False:
      print("アイテムリスト作成エラー")
      sys.exit()

   input_list_max = item_list.list_length()
   
   for Item_number in range(input_list_max):
       input_weight = int(input())
       input_value = int(input())
       item = item_f.Item()
       value_chack = item.value_set(input_value)
       if value_chack == False:
          print("アイテムの価値登録エラー")
          sys.exit()

       weight_check = item.weight_set(input_weight,input_capacity)
       if weight_check == False:
          print("アイテムの重さ登録エラー")
          sys.exit()

       item_list.list_set(item,Item_number)

   max_sum = Sum.dp_max(item_list,knapsack)
   print(max_sum)
   pass