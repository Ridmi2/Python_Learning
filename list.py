lst =[20,10,40,50]
lst1 =list((12,45,43,76))#inbuilt function

print(type(lst))
print(type(lst1))
print(lst)
print(lst1)

#how to access to the elements of a list
my_list=['Ridmi',25,'Moratuwa',False,22]
print(my_list[0])#positive indexing
print(my_list[-5])#negative indexing
#access to many characters
print(my_list)#all elements will be return
print(my_list[:])#all elements will be return
print(my_list[:3])#['Ridmi', 25, 'Moratuwa']
print(my_list[0:3])#['Ridmi', 25, 'Moratuwa']
print(my_list[3:])#[False, 22]
print(my_list[0:3:1])#['Ridmi', 25, 'Moratuwa']
print(my_list[0:3:2])#['Ridmi', 'Moratuwa']

#list inside a list 
my_list1=['Ridmi',25,'Moratuwa',False,22,[4,5,6]]
print(my_list1[5])
print(my_list1[5][0])#access to the element of the list

#can change the list in run time (mutable)
my_list1[2]='Colombo' 
print(my_list1)

#how to add one element to the list(append)
print(my_list)
my_list.append("Tharaka")#add Tharaka
print(my_list)

#how to add more than one element to the list(extend)
#my_list.extend("Tharaka")
#my_list.extend("Tharaka","Hasitha")#have to add all 2 but my vscode gives an errorthat extend also cannot call for two it is for one 

#add a element to a specific place without adding it to the ending by default
my_list.insert(2 ,'Hello')
print(my_list)

#how to remove a element (pop)
my_list.pop(6)
print(my_list)

#remove by value (remove)
my_list.remove('Ridmi')
print(my_list)

#length of list
print(len(my_list))
#how many times an element has been repeating inside the list
print(my_list.count('Moratuwa'))

#clear the all list
my_list.clear()
#using indexing
my_list[:]=[]
print(my_list)

