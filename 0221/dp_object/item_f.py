# coding : utf-8

class Item:
    def __init__(self):
        pass
    def value_get(self):
        return self._value
    def value_set(self,input):
        self._value = input
        return 0
        
    def weight_get(self):
        return self._weight
    def weight_set(self,input):
        self._weight = input
        return 0

if __name__ == "__main__":
    item = Item()
    item.weight_set(10)
    item.value_set(100)

    print("weightは",item.weight_get())
    print("valueは", item.value_get())
    pass