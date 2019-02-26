# coding : utf-8

class Item:
    def __init__(self, _item_count):
        self._item_count = _item_count
#        print("item.init = call")

    def item_count_get(self):
        return self._item_count
    def item_count_set(self, _item_count):
        self._item_count = _item_count
#        print(self._item_count)    

    def value_table_create(self, _item_count):
        self.value_table = [0 for i in range(_item_count)]
#        print(self.value_table)
    def value_table_set(self, value, _item_count):
        self.value_table[_item_count] = value
    def value_table_get(self):
        return self.value_table
    #def value_get(self, value):
    #    return self.value_table[value]

    def weight_table_create(self, _item_count):
        self.weight_table = [0 for i in range(_item_count)]
    def weight_table_set(self, weight, _item_count):
        self.weight_table[_item_count] = weight
    def weight_table_get(self):
        return self.weight_table
    #def weight_get(self, weight):
    #    return self.weight_table[weight]

if __name__ == "__main__":
    item1 = Item(0)
#    print(item1.value_table_get())
#    print(item1.weight_table_get())
#    print(item1.item_count_get())
#
#    item1.value_table_set(5,3)
#    item1.weight_table_set(1,2)
#    item1.item_count_set(7)

    item1.value_table_create(3)
    print(item1.value_table_get())