import time
def fibonacci(n):
    if n==0 or n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
   start = time.time()
   for i in range(30):
      anser = fibonacci(i)
      print(i,anser)
   elapsed_time = time.time() -start
   print("elapsed_time:{0}".format(elapsed_time) + "[sec]")