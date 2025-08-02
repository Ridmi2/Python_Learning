name = "cheese cake"


#startswith(),endswith()
print(name.startswith('c'))
print(name.startswith('r'))#check with non beginner character
print(name.startswith('chee'))#check with character collection from beginning(check with substring)

print(name.endswith('e'))#actually ending character
print(name.endswith('c'))#not the ening character
print(name.endswith('ke'))#put  a substring that ending

print(name.startswith('ese'))
print(name.startswith('ese',3))#give an index number 

x='Ridmi,25,Moratuwa'#want to replace , with the -
print(x)
print(x.replace(',','-'))
print(x.replace('i','o'))

#join
y='abc'
z='xyz'

print(y.join(z))#output is xabcyabcz
print(' '.join(z))


name2=["Rimdi","Tharaka","Wikcramasinghe"]
print(" ".join(name2))

#split
name3="Ridmi Tharaka Wickramasingeh"
print(name3.split(" "))
print(name3.split())#if don't gve the space it by default split by the space
print(name3.split("a"))
name4 = "Hasitha Dilshan\n 25 45 56"
print(name4.split("\n"))
print(name4.splitlines())#separate by \n like previous one