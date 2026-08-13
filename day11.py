'''
Lists,Tuples

#List --> Mutable,Ordered,Heterogenous

#index(),count(),copy(),sort(),reverse()

details =['codegnan',7,2018,'Hyderbad']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21)) #it returns first occurance
print(details.index(21,6))
#print(details.index('python')) #ValueError

print(details.count(21))
print(details.count('python')) #it returns 0 as we dont have it
'''
data = ['codegnan','lalitha','python','java'] #input
#output should be as follows
'''
0 : codegnan
1 : lalitha
2 : python
3 : java

for obj in data:
    print(data.index(obj),':',obj)
    
for obj in range(4):
    print(obj),':',data[obj])
    
#copy() -->shallow copy of the given collection

new = data.copy()
print(new)
print(type(new))
print(len(data))

new[2] = 'Agentic AI'
print(new)
print(data)

data.append('lalitha')
print(data)
print(new)

data = [1,4,5,[21,34,45],23]
print(data)
new = data.copy()
print(new)

new[3][4] = 'Agents' #whenever we make changes in nested list original will
#also be effected
print(new)
print(data)

new[1] = 'python'
print(new)
print(data)


marks = [14,24,-45,27,35]
print(marks)
#print(marks.sort()) #returns None
#print(marks) #returns in ascending order
marks.sort(reverse = True) #returns in Descending order...
print(marks)
marks.insert(2,'code')
#marks.sort()
#reverse() --> returns in reverese order
marks.reverse()
print(marks)
print(marks[::-1])

#type(),len(),max(),min(),print()

print(sorted('codegnan'))#returns List in ascending order
#print(sorted(['code','23',34,45])) #raises Error


#Tuples --> Tuples are Indexed,Ordered,Heterogenous,Immutable collection
#dimmensions,coordinates,database records,we prefer () for tuple notation

a = ()
print(type(a))
print(len(a))

dimensions = 1.5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))

#Operations -->Indexing,Slicing,Striding,Membership,Merging,Repetition

courses = ('PFS','JFS','DS'),'AgenticAi',[100,6,6])
print(courses)
print(len(courses))

print(courses[-2][-2:])
#courses[2] = 23 Tuples are immutable
courses[-1].append('codegnan') #we can make any modifications inside list
print(courses)

#Create a nested tuple as above and work on sliciing ,striding and list function
print('PFS' in courses) #Membership
d = courses * 2 #repetition
print(d)
e = courses + (2,3,4,5) #merging
print(e)


#Tuples Immutable -->count(),index()
print(courses..index('AgenticAI')) #returns first occurance
print(course.count('Agents'))

#print(course.sort()) #AttributeError -->sort() is in Lists not in Tuples

print(sorted(courses[-1]))
#print(sorted(courses)) #as we have mixed type

#typeCasting
d = tuple(sorted((23,12,3,4,5)))
print(d)

#accept group of integers space seperated
a,b = map(int,input("Enter the value").split())
print(a,b)

a = tuple(map(int,input("Enter the values").split(',')))
print(a)
print('9+4')
#eval() function can take any kind of input
print(eval('9+4'))

a = eval(input("Enter a list:"))#in this case u can exactly enter data as list
print(a)
print(type(a))'''


#task:Take a user input as string,do this in two days..
'''
1) give the count of each repeating character
Test case 1: programming

r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2)
r is repeating 2 times
index = [1,4]
g is repeating 2 times
index = [3,10]
m is repeating 2 times
index = [6,7]
'''



































































































































































