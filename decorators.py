def divide (a,b):
    return a/b
print(divide(0,5))
#print(divide(5,0))  #cannot be procedure gives an error

def divide (a,b):
    if b==0:
        a,b=b,a
    return a/b
print(divide(5,0))

#without changing the divide function we can change this by creating another function 
def new(func):
    def inside(a,b):
        if b==0:
            a,b=b,a
        return func(a,b)
    return inside


@new #1 0r
def divide(a,b):
    return a/b
#divide = new(divide) #2
print(divide(5,0))