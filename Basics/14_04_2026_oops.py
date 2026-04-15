# OOPS
# object oriented programming system
# class - collection of variables and functions
# class is the keyword, used to declare the class

# class Test:
#     def wish(self): # self current object of class
#         print('welcome to oops !')

# t1 = Test()
# t1.wish()        

# Example -- 2
class Test:
    # no para - no return
    def addition1(self):
        num1 = 200
        num2 = 100
        result = num1 + num2
        print(f"Sum : {result}")   
    def addition2(self):
        num1 = 200
        num2 = 100
        res = num1 + num2
        return res    
    def add3(self,num1,num2):
        res = num1 + num2
        print(f'Addition: {res}')
    # with para and with return type    
    def add4(self,num1,num2):
        res = num1 + num2
        return res
t1 = Test()         
t1.addition1()
x = t1.addition2()
print(f'sum: {x}')
t1.add3(300,100)

y = t1.add4(200,700)
print(f'Sum4: {y}')


# Example 3
# Instance Variables
# __init()__ called as constructor
# it will execute only once
# whenever we will create object, automatically constructor will execute
# class Test:
#     def __init__(self):
#         self.num1 = 10
#         self.num2 = 20

# t1 = Test()
# t2 = Test()
# t1.num1 = 200
# t1.num2 = 300

# print(f'T1 objects data {t1.num1}, {t1.num2}  T2 objects data {t2.num1} {t2.num2}')

# Example - 4
# Sharing common data to multiple objects
# class variables shared to multiple objects
# class Test:
#     company = "TCS....!" # class variable
#     def __init__(self,name):
#         self.name = name

# t1 = Test("Emp1")

# print(f'Name of employee: {t1.name} and company name {t1.company}')
# t2 = Test("Emp2")
# print(f'Name of employee: {t2.name} and company name {t2.company}')

# # Example - 5
# class Test:
#     name = "TCS....!"

# t1 = Test()
# t2 = Test()
# print(f"Name... {t1.name}")
# print(f"Name... {t2.name}")    
# Test.name = "Microsoft...!"
# print(f"Name... {t1.name}")
# print(f"Name... {t2.name}")    

# # Example - 6
# class Test:
#     name = "Apple"

# t1 = Test()
# t2 = Test()

# print(f'Name... {t1.name}')
# print(f'Name... {t2.name}')

# t1.name = "Google" # add instance variable to t1 object
# print(f'Name... {t1.name}')
# print(f'Name... {t2.name}')

# Test.name = "Microsoft"
# print(f'Name... {t1.name}')
# print(f'Name... {t2.name}')

# class Test:
#     company = "TCS..."
#     def __init__(self, name):
#         self.name = name
#     @classmethod
#     def change_company(cls,name):    
#         cls.company = name


# Test.change_company("Oracle")
# t1 = Test("Google")
# t2 = Test("Microsoft")
# print(f'Name... {Test.company}')
# print(f'Name... {Test.company}')

# print(f'Name... {t1.company}')
# print(f'Name... {t2.company}')

# Example 8 
# instance variable is priority
# first priority object level, next priority class level
class Test:
    name = "hello"
    def __init__(self,name):
        self.name = name

t1 = Test("Google")
print(f'{t1.name}')    

# Example 9
# first priority is instance variable then if it is not present we move to class variable
class Test:
    name = "hello"
    def __init__(self,name):
        #self.name = name
        pass

t1 = Test("Google")
print(f'{t1.name}')   # output hello

# Example 9
# __ is used to declare the private variables
# encapsulation
#private variables, unable to access outside the class
#private variables, unable to access with class objects
# class Test:
#     def __init__(self):
#         self.__amount = 50000

#     def display_amount(self):
#         return self.__amount

# t1 = Test()
# print(t1.display_amount())     
# print(t1._Test__amount)    

# Example 10
# Single Level Inheritance
# class Parent:
#     def test1(self):
#         print("Parent....!")

# class Child(Parent):
#     def test2(self):
#         print("Child...!")

# obj = Child()
# obj.test1()   
# obj.test2()

# # Example 11
# # Multi Level Inheritance
# class Parent:
#     def test1(self):
#         print("Parent")

# class Child(Parent):
#     def test2(self):
#         print("Child")

# class Subchild(Child):
#     def test3(self): 
#         print("SubChild")       

# obj2 = Subchild()
# obj2.test1()
# obj2.test2()
# obj2.test3()
# # Example 12
# # Multiple Inheritance
# # If function is available in Parent 1 it will execute the fn over there. If not available in Parent1 
# # then it will look into Parent 2 
# class Parent1:
#     def test(self):
#         print("Parent1")

# class Parent2:
#     def test(self):
#         print("Parent2")

# class Child(Parent1,Parent2):
#     pass

# t1 = Child()
# t1.test()

# Polymorphism
# Behaves like many
# Overriding
# Overloading


# Example 13
# overriding parent class functionality with child class functionality
class Parent:
    def db_conn(self):
        print("SQL conn soon...!")

class Child(Parent):
    def db_conn(self):
        print("No SQL Conn soon...!")

obj2 = Child()
obj2.db_conn()

# Overloading 
# Python doesn't support overloading but this functionality mimics what is function overloading
# class Test:
#     def addition(self,a,b=0,c=0):
#         print(a + b + c)

# obj = Test()
# obj.addition(10)
# obj.addition(10,20)
# obj.addition(10,20,30)

# Example-15
# Overloading
class Test:
    def addition(self,*args):
        print(sum(args))

obj = Test()
obj.addition(10,10)
obj.addition(10,20)
obj.addition(10,40,60,70)
obj.addition(10,80,90,100,200)

# # Example - 16
# class Test:
#     def addition(self, num1=None,num2=None,num3=None):
#         if num1 and num2 and num3:
#             print(num1 + num2 + num3)
#         elif num1 and num2:
#             print(num1 + num2)
#         elif num1:
#             print(num1)
#         else:
#             print(0)    

# obj = Test()
# obj.addition(10)   
# obj.addition(10,20)   
# obj.addition(10,20,40)            
# obj.addition()         
# Example 17
# __add__ is predefined function and it will break object n1 and get value and then add the value of n2's object
class Test:
    def __init__(self,num1):
        self.num1 = num1
    def __add__(self,other):
        return self.num1 + other.num1

n1 = Test(10)
n2 = Test(60)
print(n1 + n2)
# Example 18
# Dunder Methods
# If we don't use __str__() then it will give hashcode for Test Object
# If we use the __str__() then it will override the hashcode and return whatever message we want to say
class Test:
    def __str__(self):
        return "Welcome"

obj = Test()
print(obj)

# if we know the function name but don't know implementation then we call the method as abstract method
# Decorator @abstractmethod is added to function to make it abstract

from abc import ABC,abstractmethod

class Business(ABC):
    @abstractmethod
    def start_business(self):
        pass
    def make_docs(self):
        print("make necessary docs")    
class Friend(Business):
    def start_business(self):
        print("Initiate AI startup company")
    

obj = Friend()
obj.start_business()        
obj.make_docs()

# Example 20
# self - instance methods 
# cls - class methods
# nothing present in function paramter then it is static method
class Parent:
    def test1(self):
        print("hello")

class Child(Parent):
    def test2(self):
        return super().test1()

obj = Child()
obj.test2()        

# Example 21
class Parent:
    def __init__(self, param1):
        self.param1 = param1

class Child(Parent):
    def __init__(self,param1, param2):
        super().__init__(param1)
        self.param2 = param2

obj = Child(200,300)
print(obj.param1 + obj.param2)