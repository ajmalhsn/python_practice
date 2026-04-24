# mutable
# unorderd(<3.7), ordered(3.7+)
d1 = {"num2": 100,"num1":200}
print(d1)

d2 = dict(num2=100,num1=200)

print(d2)

d3 = dict([("num1",100),("num2",200)])

print(d3)

d4 = {}

print(d4)

# access
#print(d1["num3"]) ## not safe reading, pgm will fail and report key error
# print(d1.get("num3")) ## safe reading, pgm will not fail and give none value
# ## update
# d1["num1"] = 300
# d1["num3"] = 3000

# d1.update({"num1":200,"num2":600,"num3":3000,"num4":50000})
# # delete 
# del d1["num1"]
# print(d1)

# print(d1.pop("num2"))
# print(d1)
# d1.popitem()

# print(d1)
# # delete all
# d1.clear()
# print(d1)

for k in d1:
    print(k)
for v in d1.values():
    print(v)   

for k,v in d1.items():
    print(k,v)

print(d1.keys())    
print(d1.values())
print(d1.items())

d1 = {x:x*x for x in range(5) if x%2 == 0}
print(d1)

students = {
    "s1": {"name":"Std1","marks": 80},
    "s2": {"name":"Std2","marks": 90}
}
print(students["s1"]["name"])
for k,v in students.items():
    for k,v in students[k].items():
        print(k,v)
d1 = {
    "num1": 100
}
#d2 = d1.copy() # shallow copy
#d1 = d2  # reference copy
# d2["num3"] = 300
# print(d2)
# print(d1)

d1 = {
    10 : "Hello",
    10.1 : "Welcome",
    10.1 : "Bye",
    "str1": "Python",
    (1,2): "Dict",
    True: "Hi",
    None: "Hello"
   # [10,20]: "Hello"
}
print(d1)

str = "aabbcc"
freq = {}
for ch in str:
    freq[ch] = freq.get(ch,0) + 1

print(freq)
d1 = {"a":2,"c":8,"b":6}
print(sorted(d1.items(),key=lambda x:x[0]))