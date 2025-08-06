lst = [3,5,7]
for i in lst:
    print(i)

list={4,6,7}    
itr=iter(list)
print(next(itr))
print(next(itr))

#can use a while loop also
list={4,6,7}    
itr=iter(list)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break    