# coding : utf-8

import item_f

class Item_list:
    def __init__(self):
        pass
    def list_create(self,input_list_max):
        if 1 <= input_list_max and input_list_max <= 100:
            self._item = [0 for i in range(input_list_max)]
            return True
        else:
            return False

    def list_get(self,Item_number):
        return self._item[Item_number]


    def list_set(self,item,Item_number):
            self._item[Item_number] = item
    
    def list_length(self):
        return len(self._item)

if __name__ == "__main__":
    item_list1 = Item_list()
    item1 = item_f.Item()

    item_list1.list_Create(10)

    item1.value_set(10)
    item1.weight_set(100)

    for i in range(10):
        item_list1.item_list_set(item1,i)
        print("リスト",i,"の価値は",item_list1.item_list_get(i).value_get())
        print("リスト",i,"の重さは",item_list1.item_list_get(i).weight_get())
    
