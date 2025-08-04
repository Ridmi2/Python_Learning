def area(x):
    return x*x
print(area(4))

#for small functions as above can be written without def 
#cannot be use for complex one,only one row calculation can be done
area = lambda x:x*x
print(area(5))

#areaa of a rectangle
area = lambda x,y:x*y
print(area(2,4))

#use inside a function 
def apple (unit_price):
    return(lambda number_of_apples: number_of_apples*unit_price)
x=apple(48)
print(x(12))