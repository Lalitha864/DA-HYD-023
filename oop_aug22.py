'''
#Students details with mutiple objects
class Students:
    """Understanding the usage of OOP"""
    def data(self,name,id,gender,email_id):
        self.name = name
        self.id = id
        self.gender = gender
        self.email_id = email_id
    
#Create a class with car brand name,price,color --> display()
class Cars:
    """Understanding the usage of OOP"""
    def car_data(self,brand,name,price,color):
        self.brand = brand
        self.name = name
        self.price = price
        self.color = color
    #Methods(behaviour)
    def details(self):
        print(f'Car Brand is {self.Brand}')
        print(f'Car Model Name is {self.name}')
        print(f'Car Color is {self.Color}')
        print(f'Car Price is {self.Price}')
u1 = Cars("Tata","Nexon","9lakhs","Blue")
u1.details()

'''
'''
#Construct -->Instances methods -->Public Attributes
#Encapsulation
#Constructor -->It is a special method(__init__())
#which will automatically initialize the attributes and the methods to the objects in the class
'''
'''
class Cars:
    """Understanding the usage of Constructor in  OOP"""
    def __init__(self,brand,name,price,color):
        self.brand = brand
        self.name = name
        self.price = price
        self.color = color
    #Methods(behaviour)
    def details(self):
        print(f'Car Brand is {self.Brand}')
        print(f'Car Model Name is {self.name}')
        print(f'Car Color is {self.Color}')
        print(f'Car Price is {self.Price}')
#u1 = Cars("Tata","Nexon","9lakhs","Blue")
#u1.details()
'''
'''
class Cars:
    """Understanding the usage of Constructor in  OOP"""
    def __init__(self):
        self.brand = "BMW"
        self.name = "Sedans"
        self.price = "50Lakhs"
        self.color = "White"
    #Methods(behaviour)
    def details(self):
        print(f'Car Brand is {self.brand}')
        print(f'Car Model Name is {self.name}')
        print(f'Car Color is {self.color}')
        print(f'Car Price is {self.price}')
u1 = Cars()
print(u1.brand,u1.name,u1.color,u1.price)
u1.details()'''

'''
#Encapsulation --> It is one of the main feature of OOP.
It binds (bundles) the data (attributes) and the methods (behaviour)
into single unit (class) -->multiple objects
-->Attributes --> Public,Protected,Private
#Public Attributes --> Attributes defined inside the class
and can be modified outside the class

class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username):
        self.user = username #Public Attribute
    #To access student details
    def display(self):
         print(f'Student Username is {self.user}')
u1 = CodegnanPortal("Javeed")
u1.display()
u1.user = "Javeed"
u1.display()
print(u1.__dict__) #returns the key-value pairs for attributes
u2 = CodegnanPortal("Shaik")
u2.display()
print(u2.__dict__)'''
'''
#Protected attributes --> we use single underscore before an
#attribute moreover it can be modified also outside the class
#and even accessible in subclasses....
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp):
       self.user = username #Public attribute
       self._otp = _otp #protected attribute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has received OTP as {self._otp}')
u1 = CodegnanPortal("Lalitha",23456)
u1.display()
u1._otp = 3456
u1.display()
'''
'''
#Protected attributes --> we use single underscore before an
#attribute moreover it can be modified also outside the class
#and even accessible in subclasses...

class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp,password):
        self.user = username #Public attribute
        self._otp = _otp #protected attribute
        self._password = password #private attribute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has received OTP as {self._otp}')
u1 = CodegnanPortal("Javeed",12345,"admin123")
#print(u1.password) AttributeError as password is private
print(u1.__dict__)
print(u1._CodegnanPortal__password) #NameMangling
'''
#In above case we are using NameMangling but the right way is
#usage of getter() and setter() methods

class CodegnanPortal:
    def __init__(self,username,_otp,password):
        self.user = username #Public Attribute
        self._otp = otp #protected attribute
        self.__password = password #private attribute
    #Usage of getter() method
    def get_password(self):
        return "******"
    #to modify the password we use setter() method
    def set_password(self,new_password):
        if len(new_password) < 6:
            print("Wrong Password not satisfied 6 characters")
        else:
            self.__password = new_password
            print("Now password is updated")
u1 = CodegnanPortal("Lalitha",23456,"admin123")
print(u1.get_password())
u1.set_password("Lalitha")
u1.set_password("Lalitha123") #compulsory morethan 6
print(u1.get_password())