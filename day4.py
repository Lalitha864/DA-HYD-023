'''
Identity Operators -->checks the identity of an object --> id()

a = 5
b = a
print(id(a))
print(id(b))
c = 5
print(id(c))
print(a is c)
print(5 == 5)

a = [1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))
#As we have Lists (Mutable Collection)
#ids whereas values are same
print(c is a) #output False
print(c == a) #output True
print(a is not c)


#Bitwise Operators --> we perform bitwise operations over operands
#& (and), | (or),^(XOR),shifiting operators (<<,>>)
#Number will be converted to binary format

print(5&3) #both 5 and 3 to be converted binary and bitwise and is performed

print(5|3) #bitwise OR

print(5^3) #Bitwise XOR

print(5 and 3) #here and is logical operator checks for both existances
#returns 5 in above case

print(5 or 3) #returns 3 in this case

#Leftshift Operator << ,right shift Operator >>

print(5 < 1) #false comparision
print(5 << 1)#Left shift operation by 1 position
print(5 >> 1)#right shift operation

print(15 << 2) #convert 15 to binary and perform 2 times shifting

print(15 >> 2) #same 2 times right shifting


#Input Formatting --> input(),int(input()),float(input())
#You know -->single input
#2 or 3 inputs --> map()
#group of integers --> list(map(int,input().split(','))

names = input("Enter the name:").split(',')
print(names)

name1,name2 = map(str,input("Enter the Friends Names:").split(','))
print(name1,name2)
'''
#Tokens --> Numeric Datatypes --> Operators -->Flow of the program
#Control Block Statements
#Conditional Statements --> if,else,elif (rely on condition to be executed)
#Repetition Statements (Loops) --> for,while

#Conditional Statement --> if usage
'''
syntax :

if <condition>:
    statement(s)...
    ......

#age = 15
age = int(input("Enter the age:"))
if age>=18 and age in [19,21,20]:
    print('Your age is:',age)
print(age)

#else keyword --> if false

else:
    statement(s)..
    ....
else:
    statement(s).....
    ....


#Vote Eligiblity ->To check his/her voter eligibility and give access...

age = int(input("Enter the age:"))
if age>=18:
    print("You have Voter eligibility and age is",age)
    print("Access Granted")
else:
    age = 18-age
    print("You dont have eligiblity as your age is",age,"years")
    print("You need to wait for more",age,"years")

#same case let's use only nested --> if else
if age >0:
    if age>=18:
        print("You have voter eligiblity and age is",age)
        print("Access Granted")
    else:
        age = 18-age
        #print("You dont have eligiblity as your age is",age,"Years")
        print("you need to wait for more",age"years")
else:
    print("You have entered -ve values/zero enter only +ve")

task : Students marks and grade analayzer
90 - 100 --> 'A'
80 - 89 --> 'B'




















































