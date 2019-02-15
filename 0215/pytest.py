def main(i):
    months = [ 'Jan', 'Feb', 'Mar', 'Apr',
            'May', 'Jun', 'Jul', 'Aug',
            'Sep', 'Oct', 'Nov', 'Dec' ] 
            # []でまとめて入れることができるが、printで呼ぶと[]も出てくる。
            #また、これはlistの宣言である。

    print (months[i-1]) # #は//と同じ意味を持つ
    return months[i]

class months:
    Jan = 1
    Feb = 2
    Mar = 3

if __name__ == "__main__": #mainと同じ意味をもつ
    for i in range(12):
        if i == 6:
            print(i+1,main(i) + " if") 
        elif i == 7:
            print(i+1,main(i) + " else if")
        else :
            print(i+1,main(i) + " else")         
            
    a = months.Feb
    print(a)           
    