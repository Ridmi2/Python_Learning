def test ():
    yield 4
y=test()    
print(next(y))


def test (a):
    for i in a:
     yield i
y=test([2,3,4,5])    
print(next(y))
print(next(y))

def fib():
   a,b =0,1
   while True:
      c=a+b
      yield a
      a,b = b,c
y =fib()
print(next(y))   
print(next(y))  
print(next(y)) 
print(next(y))  