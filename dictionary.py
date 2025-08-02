my_dict ={'name':'Ridmi','age':25,'city':'Moratuwa'}
students={80:'Tharaka',81:'Hasitha',82:'Dilshan'}
print(my_dict)

#access values
print(my_dict['age'])

print(my_dict.get('name'))


#change the dictionary
my_dict['name']='Sehiru'
print(my_dict)

#add new data to the dictionary
my_dict['ismarried']=False
print(my_dict)


#addd many values
my_dict.update({'gender':'male','score':90})
print(my_dict)

#remove by del
del my_dict['age']
print(my_dict)
 #remove by pop

my_dict.pop('score')
print(my_dict.pop('score',"Not found"))

print(my_dict)

#clear all
my_dict.clear()
print(my_dict)