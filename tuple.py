tpl1=(3,5,6,3,9)
print(type(tpl1))
print(tpl1)
#or
#tpl2=tuple((56,34,46))
#print(type(tpl2))
#print(tpl2)

#print by indexing
print(tpl1[0])
print(tpl1[1:])
print(tpl1[2:4])

#tpl1[1]=43#cannot because it is immutable 

#count of the repeatable elements
print(tpl1.count(3))

#get the value by index
print(tpl1.index(3))

#convert list into a tuple
lst =[2,4,6]
tpl = tuple(lst)
print(tpl)
print(type(tpl))