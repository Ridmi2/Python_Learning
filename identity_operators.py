x= 10
y=10

z=8

print(x is y)  # True, because x and y point to the same object
print(x is not z)  # True, because x and z point to different objects
print(x is not y)  # False, because x and y point to the same object
print(x is z)  # False, because x and z point to different objects

print(id(x))  # Prints the memory address of x
print(id(y))  # Prints the memory address of y
print(id(z))  # Prints the memory address of z


x= [1, 2, 3]
y= [1, 2, 3]

print(x is y)  # False, because x and y are different lists in memory
print(x==y) # True, because x and y have the same content