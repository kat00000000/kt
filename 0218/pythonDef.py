
def add(a):
    top =a[0]
    bottom = a[0]

    for i in a:
        if top < i:
            top = i
        if i < bottom:
            bottom = i
    return top,bottom

if __name__ == "__main__":
    a = [10,2,3,4]
    print(add(a))
    myfunc = lambda x,y:x + y

    print(myfunc(5,5))
