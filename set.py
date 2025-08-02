my_set ={34,45,7,48}
print(my_set)#{48, 34, 45, 7}
print(type(my_set))
#cannot be use the indexing 

#add
my_set.add(47)
print(my_set)#but cannot predictable of which place that element would be added in the set

#remove
my_set.remove(48)
print(my_set)

A={1,2,3,5,7}
B={5,7,9,10,11}

#union
print(A.union(B))
print(B.union(A))#same result

#intersection
print(A.intersection(B))
print(B.intersection(A))#same

#differnce
print(A.difference(B))
print(B.difference(A))

my_set.add('Rimdi')#only one can add 
my_set.add(('Rimdi','Tharaka'))#can add a tuple
print(my_set)

#add more than one element
my_set.update(('HAsitha','Dilshan'))
print(my_set)

#remove method
my_set.remove('Rimdi')#if you try to remove unavailable elemnt it gives an error
print(my_set)

#discard
my_set.discard('Rimdi')#it did not gives an error even it is not available
print(my_set)

#pop remove any value it chooses
my_set.pop()
print(my_set)
my_set.pop()
print(my_set)

#clear the whole set
my_set.clear()
print(my_set)