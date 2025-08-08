import os
#x=open('test.txt', 'r')
#print(x.read())

#one line for reading
#x=open('test.txt', 'r')
#print(x.readline(),end='')#to remove the space you have to end this line 
#print(x.readline())

#read all lines
#x=open('test.txt', 'r')
#print(x.readlines())
#x.close()

#write mode
#x=open('test.txt', 'w')
#x.write('Ridmi Wickramasinghe\n')
#x.close

#append mode
#x=open('test.txt', 'a')
#x.write('Ridmi\n')
#x.write('Wickramasinghe\n')
#x.close()

#x=open('hi.txt', 'w')#create a new file

#emove a file with os
#os.remove('hi.txt') 

#rename a file with os
#os.rename('test.txt', 'test1.txt')

#check if a file exists
print(os.path.exists('test1.txt'))#returns True or False
print(os.path.abspath('test1.txt'))#returns the absolute path of the file
print(os.path.getsize('test1.txt'))#returns the size of the file in bytes