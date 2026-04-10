num1 = 200
num2 = 300

addition = num1 + num2
print("The addition of num1 and num2 is: ", addition)
print(type(addition))

num3 = 10.5
num4 = -20.5

res1 = num3 + num4;
print("The addition of num3 and num4 is: ", res1)
print(type(res1))


#string
# collection of characters

# "" (double quotes)  '' (single quotes)  """ """ (triple quotes)

str1 = "Hello Python"
str2 = 'Hello, Python Variables!!!'
str3 = """
        Hello Team
        This is python multi line string
        Time: 9AM
            """

print(str1)
print(str2)
print(str3)

str = "Hello"
# print(str[0]) # first letter from left
# print(str[-1]) # first letter from right
# print(str[0:2]) # starts from 0 to 2 
# print(str[:2]) # starts from 0 to 2
# print(str[2:]) # starts from 2 till end
print(str[::-2]) # reverse the string


# strings are immutable
# str = "Python"
# str[0] = 'H'

str = "Python"

str1 = "p" + str[1:]
print(str1)

str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)
print(str1 * 3) # makes the string appears 3 times


print("Py" in "Python")
print("Java" not in "Python")
str = "Python"
for ch in str:
    print(ch)

str = "DataScience"
msg = f"welcome to {str}"
print(msg)


print("Hello\nWorld")
print("Hello\tWorld")
print("Welcome to \"Data Science\"")
print("it\'s a Data Science course")
print("C:\\Users\\Python")

str = "python"
new_str = str.replace("p","y")
print(new_str)
print(str)

#Booleans

#True - 1
#False - 0 
flag1 = True
flag2 = False

print(flag1)
print(flag2)
print(flag1 + 1)
print(flag1 + flag2)

age=18
if age>= 18:
    print("Major !!!")
else:
    print("Minor !!!")

print("Major" if age>18 else "Minor")         

#None ---> No Value / Nothing / "Empty but not zero"

x = None
print(x)
print(type(x))

# list
# []
# collection of elements
#hetrogenous
# Duplicates
# Ordered
# mutable
list1 = [10,50,20,30,40, "Hello", 'h1']
list1.append(60)
print(list1)
list2 = [10,20,30,40,50]
print(list2[1])
print(list2[-4])

# tuple
# collection of elements
# ()
#hetrogenous
# Duplicates
# Ordered
# immutable
tuple1 = ("Hello", "my Name is ", 20,30,40,60, True, 10.1)
print(tuple1)


# dictionary
# key and value
d1 = {
    "name": "Value",
    "sub": "Gen AI",
    "cloud": "MLops, LLM"
}
print(d1["name"])
d1["sub"] = "Gen AI and agentic AI"
print(d1["sub"])
del d1["sub"]
print(d1)

# Set
# collection of elements
# {}
# no duplicates
# no order
# Hetrogenous

s1 = {2,2,2,3,1,1,1,6,6,6, None, "Hello"}
print(s1)
print(type(s1))
print(len(s1))

# int
# float
# str
# list
# boolean
# tuple
# dict
# None
# set


