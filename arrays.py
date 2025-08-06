from array import*
x= array('I',[2,3,4,5,6]) #only positive integers 
print (x)
print(x[0])
print(x[1:3])
x.insert(2,6)
print(x)

x.append(9)#only one element will be added o the array
print(x)
x.extend([8,9,10])#more than one to be added to the array
print(x)

x.pop()
print(x)
x.remove(8)
print(x)
y=array('I',[37,19,53])
for i in range(len(y)):
    print(y[i])
z=x+y#join
print(z)

