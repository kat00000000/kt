# coding : utf-8

import item_f

class Item_list:
    def __init__(self):
        pass
    def list_Create(self,input):
        self._item = [0 for i in range(input)]
        return 0
    def item_list_get(self,Item_number):
        return self._item[Item_number]


    def item_list_set(self,item,Item_number):
        if Item_number < 0 and (len(self._item)-1) < Item_number:
            return 1
        else:
            self._item[Item_number] = item
            return 0
    def item_length(self):
        print(len(self._item))
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
    
