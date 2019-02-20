#coding : utf-8
import knapsack
import item
import item_list

if __name__ == "__main__":
   
   inputN = 10
   knapsack1 = knapsack.Knapsack(10)
   knapsack1.capacity_set(1)

   item1 = item.Item()
   item1.value_set(10)
   item1.weight_set(20)
  
   item_list1 = item_list.Item_list()
   item_list1.list_Create(inputN)
   
   for i in range(inputN):
    item_list1.item_list_set(item1,i)

   print("ナップサックの容量は",knapsack1.capacity_get())
   print("アイテムの価値、重さ",item1.value_get(),item1.weight_get())
   
   for i in range(inputN):
       tempV = item_list1.item_list_get(i).value_get()
       tempW = item_list1.item_list_get(i).weight_get()
       print("アイテム配列",i,"の価値、重さ",tempV,tempW)
   pass