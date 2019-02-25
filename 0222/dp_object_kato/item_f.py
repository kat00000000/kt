# coding : utf-8

class Item:
    def __init__(self):
        pass

    def value_get(self):
        return self._value

    def value_set(self,input_value):
        if 1 <= input_value and input_value <= 1000000000:
            self._value = input_value
            return True
        else:
            return False
        
    def weight_get(self):
        return self._weight

    def weight_set(self,input_weight,input_capacity):
        if 1 <= input_weight and input_weight <= input_capacity:
            self._weight = input_weight
            return True
        else:
            return False

if __name__ == "__main__":
    item = Item()
    item.weight_set(10)
    item.value_set(100)

    print("weightは",item.weight_get())
    print("valueは", item.value_get())
    pass