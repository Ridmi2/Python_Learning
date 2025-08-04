from functools import reduce

#filter
number=[1,2,3,4,5,6,7,8]

def even_num (x):
    return x%2 ==0
y=list(filter(even_num,number))
print(y)

# filter using lambda
number=[1,2,3,4,5,6,7,8]
y =list(filter(lambda x:x%2==0,number))
print(y)

#map function
number=[1,2,3,4,5,6,7,8]
y=list(map(lambda x:x*2,number))
print(y)

#reduce function 
number=[1,2,3,4,5,6,7,8]
sum=reduce(lambda x,y:x+y,number)
print(sum)