
def add(a):
    top =a[0]
    bottom = a[0]

    for i in a:
        if top < i:
            top = i
        if i < bottom:
            bottom = i
    return top,bottom

class MyClass:
    def __init__(self):
        self.data = (1,2,3,4)
        self.index = 0
    def __iter__(self):
        return self
    def next(self):
        if self.index < len(self.data):
            self.index　+= 1
            return self.data[self.index -1]
        else:
            raise StopIteration

if __name__ == "__main__":
    a = [10,2,3,4]
    print(add(a))
    myfunc = lambda x,y:x + y

    print(myfunc(5,5))

    for n in MyClass():
        print n
