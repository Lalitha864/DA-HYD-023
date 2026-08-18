'''
Tokens,Datatypes -->Control Flow Statements -->if,else,for,while,break
continue..

Procedure Oriented programming

Functions -->A function is a block of code which performs a specific task
Its a reusable group of statements where we define using
def keyword
Advantages --> Code reusability,code maintainability,ease of debuggin
avoding code duplication...

def fname(parameters):
    """Doc String"""
    statements(s).....
    ...........
    return value(s).....
fname(args)

#To Perform sum of given objects
def add(a,b):
    """Sum of objects"""
    c = a+b
    return c
print(add(12,3))
print(add('code','gnan')) #concatenation
print(add([12,5],[12,34])) #Merging
c,d = map(int,input("Enter the values:").split(','))
print(c,d)
print(add(c,d))


def add(a,b)
    """Sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,-34)) #it returns result along with None

name,age,salary = "saketh",32,50000
#usage of return

def details():
    #return name,age,salary
    #return "codegnan"
    #return 23+34+45
    return 3it returns None as output
print(details())

There are 5 types of arguments:
-->Positional Arguments
-->Default arguments
-->keyword arguments
-->Variable length arguments (*args)
-->Keywords variable length arguments (**kwargs)

#Positional Aruguments --> Number of arugments in functions defn should
#match with function call (order has to be maintained)
#print(len(123,234)) this is as per bulit-in len(obj) will accept one argument

def details(name,place):
    """To store the details"""
    #name = "codegnan"
    #place = "Hyderbad"
    return name,place
print(details("saketh","codegnan"))
print(details("sai","vizag"))
#print(details("vizag","shyam",34)) #raises TypeError as only 2 arguments to
c,d = map(str,input("Enter the value").split(','))
details(c,d)

#Default arguments -->we can make arguments as default but not first arguments
#as default

#def grocery(item,price=35):
#def grocery(item="cheese",price=100): #we can also make all args as default
def grocery(item="Burger",price): #non default always follow default
    """usage of default arguments"""
    print(f'the item is {item} and price is {price}')

grocery("Milk",32)
#grocery(32,"Milk")
grocery("Bread") #by default we have given price as 35
grocery("Bread",45)
'''

#keywords arguments -->Whenever we want to specify the name of argument
def employee(name,salary,role,place="Codegnan"):
    """Keyword arguments usage"""
    print(f'Employee name is {name},role is {role} and salary is {salary},\
          works in {place}')
employee("sai",20000,"Admin")
employee(salary = 25000,role = "Frontdesk",name ="sravya")

















































































































































