class Item:
    def __init__(self):
        self.value
        self.weight
    def value_get(self):
        return self.value
    def value_set(self,input):
        self.value = input
    def weight_get(self):
        return self.weight
    def weight_set(self,input):
        self.weight = input

if __name__ == "__main__":
    item = Item()
    item.weight_set(10)
    item.value_set(100)

    print("weightは" + item.weight_get)
    print("valueは" + item.value_get)
    pass