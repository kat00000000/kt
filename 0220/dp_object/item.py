# coding : utf-8

class Item:
    def __init__(self):
        self.value = 0
        self.weight = 0
    def value_get(self):
        return self.value
    def value_set(self,input):
        self.value = input
        return 0
        
    def weight_get(self):
        return self.weight
    def weight_set(self,input):
        self.weight = input
        return 0

if __name__ == "__main__":
    item = Item()
    item.weight_set(10)
    item.value_set(100)

    print("weightは",item.weight_get())
    print("valueは", item.value_get())
    pass