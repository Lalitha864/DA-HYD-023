'''
Sequences --> Strings,Lists,Tuples,Sets
Mapping -->Dictinory

#Lists --> Collection of heterogenous elements(items)
#List -->Indexed,Ordered,Mutable,Hetergrogenous,we use [] to store the data

marks = [35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)
#Operations : Indexing,Slicing,Striding,Membership,Merging,Repetition

#Nested Lists --> A list inside another list

names  = ['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(len(names))
print(names[0])
print(name[3])
print(name[-3])

print(type(name[0])
print(names[0][:4]) #it returns code
print(name[0][4:])

#get the output as cdga
print(names[0][::2])
names[0] = names[0][::-1])
print(names)

print(names[3])
print(len(names[3]))
print(names[3][2])
#Indexing,Slicing -->Mutable
names[2] = 'python'
print(names)
#By indexing if we change the elements,lengths of collection will remain same
name[4] = ['codegnan','PFS',JFS','DA','AAA','DS']
print(names)
print(len(names))
print(names[4],[0][4:])

names[2:4] = 'Abhiram','saketh','python','java'
print(names)

#In slicing whatever elements u pass as per the logic length keeps on increases

#o/p as follows :
#['Codegnan',25,'Abhiram','python','Saketh','java','DA23',34]
names[3:6:2] = ['python','java']
print(names)

#create a nested list with strings,lists and work on Indxing,Slicing,Striding
#added advantage if u could add string functions also to it
#Lists Functions -->append(),insert(),extend(),pop(),remove(),clear()
#index(),count(),copy(),sort(),reverse()

names = ['codegnan','saketh']
#append() -->inserts single element to the end of the list
names.append('data')
#print(names)
#names.append('analysis','agents') #TypeError
names.append(['analysis','agents'])
#print(names)
#append() will always increment the length of list by 1
#print(names[3])
names[3].append('chatgpt')
#on list not print
print(names[3])
print(names)
#extend() -->inserts multiple elements to the end of list

names.extend('analysis') #string will ben splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,75,24,56])
print(names)
#names.extend(35,45) TypeError
#print(names)

names.insert(1;'python')
print(names)
names.insert(0,'java')
print(names)
print(names)#names.insert([1:4],['a','b']) #syntaxError
#print(names)
names.insert(-1,'AAA')
print(names)
'''
#pop(),remove(),clear()
#pop() by default last ,else given index
#pop(),remove(),clear()
#pop() by default last,else given index
print(names.pop())
print(names)
names.pop(2)
print(names)

names.remove(14)
print(names)
#names






































































































      
