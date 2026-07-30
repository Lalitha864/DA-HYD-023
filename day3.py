#Numeric datatype --> int,float,complex along with boolean

#Input formatting -->Accepting input from the user -->input()

#Accepting integer input from user
#by default input() accepts any input --> str
#int (input()) --> will accept only intergers
'''age = float(input('Enter the age:'))
print(age)
print(type(age))

#float(input()) -->accepts intergers,float values
age = float(input('Enter the age:'))
print(age)
print(type(age))

#Accepting string input from user

name = input("Enter the name:")
print(name)
print(type(name))

#Accept group of values

marks = int(input("Enter the marks:"))
print(marks)

a = input().split() #by default split() has space
print(a)

#space seperated values
a = input().split() #now enter spaces in output
print(a)
#comma seperated values
a = input("Enter the values:").split('&')
print(a)

#List of integers
marks = list(map(int,input("Enter the values").split(',')))
print(marks)

#Now we want to accept 2 values from user
age,salary = map(int,input("Enter the values").split(','))
print(age)
print(salary)

#Single input --> int(input())
#two inputs -->a,b = map(int,input().split(',')
#any number result as list --> a = list(map(int,input().split(','))

#float of intergers
marks = list(map(float,input("Enter the values").split(',')))
print(marks)

#group of float values
age,salary = map(float,input("Enter the values").split(','))
print(age)

#Accepting input from user --> int,float -> input formatting

#Operators --> Operators perform operators between values (operands)
#7 types -->Arithmetic,Assignments,comparsion (Relationship)
#Membership,Identity,Logical,Bitwise

#Arithmetic Operators -->Arithmetic operations
#+ , - , *,/
print(5+6)
print(5-6)
print(5*6)
print(5/6) #float value
#floor Division (integer division) -->returns quotient
print(5//6)
#Modulus -->divisible rules ->returns remainder
print(5%6)
#power (exponential)
print(5**6)

#Task-->Accept integer input as length,breadth -->find the area of rectangle
#Area = length * breadth
l = int(input("Enter the length"))
b = int(input("Enter the breadth"))
area = l*b
print(area)

#Assignment operators -->assign the values
# = , += , -=
a = 45
print(a)
#update the value of a
a = a + 5 #a+= 5
print(a)
b = 35
b += a #b = b + a
print(b)
b -= 5 #b = b-5
print(b)

#Task : *=,/=,//,%=,**= workout

#comparision Operators -->we compare the values -->boolean
# == (equal to) , != (not equal to) , < (less than) , >(greater than)
# <= (less than or equal to) >= (greater than or equal to)

age = 21
print(age == 21) #returns boolean output
print(age != 31)
print(age < 21)
print(age <=21)
print(age > 31)
print(age >= 31)

print(-5 < -1)


#Membership Operators --> in not in -->boolean
#it checks for the existance of an object in a collection

marks = [56,75,45,85]
print(35 in marks)
#print(35 in 355) #TypeError

print(25 not in marks)
print('code' in 'codegnan')
print('$' in 'abc$frg')


#Logical Operators --> logical decision making -->and,or,not
#and -->all conditions to be satisfied
#or --> any one condition to be satisfied

a = (25 in [25,45,65]) and 45 < 56
print(a)
b = 45 > 56 or 25 <= 45
print(b)
c = not True
print(c)

#Identity Operators --> check for identity of an object --> id()

a = 35
b = 35
print(id(a))
print(id(b))
print(a is b)
c = a
print(id(c))
print(c is a)
'''
a = [1,2,3,4,5]
print(id(a))
c = a
print(id(c))
print(c is a)
b = [1,2,3,4,5]
print(id(b))





















































































































