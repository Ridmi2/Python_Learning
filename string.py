name = 'SriLanka'

print(name)
#want to access the first string 
print(name[0])
print(name[3])
print(name[-1])
print(name[3:7])

print(name[0:3])#want the beginning character set Sri
print(name[:3])#this also gives Sri without the start index
print(name[3:8])#until the end of the word
print(name[3:])#also until the end of the 

#how to concat two strings
n1='Python'
n2 ='Programming'
n3 =46
##this gives an error because we concat int type data with string
print (n1+' '+n2+' '+str(n3))

#in/not in 
name = 'Ridmi'
print('R' in name)#check whether R is in the name
print('t' in name)