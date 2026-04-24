import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]
#plt.plot(x,y,color="red")

# plt.plot(x,y,color='orange',linestyle='--',marker='x') # linestyle "-","--",":"  marker = "o","x","*"
# plt.xlabel("X Axis")
# plt.ylabel("Y axis")
# plt.title("Line Plot")

# plt.show()

# stds = ["Std1","Std2","Std3","Std4","Std5","Std6","Std7"]
# marks = [40,50,80,90,80,70,70]
# # plt.bar(stds,marks,color=["red","blue","green"],width=0.5,edgecolor='black')
# bars = plt.bar(stds,marks,color=["red","blue","green"],edgecolor='black')
# for bar in bars:
#     plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height()+ 1,bar.get_height(),ha="center",va="center")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.show()

# Pie Chart
# subjects = ["Math","Science","English","Computer"]
# marks = [80,90,70,95]
# # 1.digit represents the fractional digits after . to show in pie chart
# # 
# explode = [0,0.1,0.2,0]
# plt.pie(marks,
#         labels=subjects,
#         colors=["gold","lightblue","green","grey"],
#         autopct='%1.2f%%',
#         explode=explode,
#         shadow=True,
#         textprops={'fontsize':12},
#         wedgeprops={'edgecolor':'black','linewidth':3},
#         startangle=90)
# plt.title("Students Marks Distribution")
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.show()

# marks = [45,50,55,56,57,60,67,70,80,82,58,62,72,83,82,85,88,90,100]
# max = 100
# min = 45
# diff = 100-45 = 55
# bin size = 55 / 5 = 11
# bin1 = 45 - 56 ( 45 included, 56 excluded)
# bin2 = 56 - 67 ( 56 included, 67 excluded)

# last bin last vlaue included
# plt.figure(figsize=(7,5))
# plt.hist(marks,bins=5,color='aqua',edgecolor='black')
# plt.xlabel("Marks")
# plt.ylabel("Frequency")
# plt.show()

# Scatter
# hours = [1,2,3,4,5,6]
# marks = [35,40,45,55,70,80]
# plt.figure(figsize=(8,6))

# plt.scatter(hours,
#             marks,
#             s=100,
#             color='red',
#             marker='x',
#             edgecolors='yellow',
#             alpha=0.7)
# #plt.plot(hours, marks, color='blue', linestyle='--')
# plt.grid(True)
# plt.show()


# Area Graph

# months = ['Jan','Feb','March','April','May']
# sales = [100,150,200,300,50]

# plt.fill_between(months,sales)
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.title("Monthly Sales Graph")

# plt.show()

plt.figure(figsize=(8,6))
plt.subplot(2,2,1)
x = [1,2,3,4]
y = [10,20,30,50]
plt.plot(x,y)

plt.subplot(2,2,2)
plt.bar(x,y)

plt.subplot(2,2,3)
marks = [45,50,55,56,57,60,67,70,80,82,58,62,72,83,82,85,88,90,100]
plt.hist(marks,bins=5,color='aqua',edgecolor='black')
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.subplot(2,2,4)
subjects = ["Math","Science","English","Computer"]
marks = [80,90,70,95]
# 1.digit represents the fractional digits after . to show in pie chart
# 
explode = [0,0.1,0.2,0]
plt.pie(marks,
        labels=subjects,
        colors=["gold","lightblue","green","grey"],
        autopct='%1.2f%%',
        explode=explode,
        shadow=True,
        textprops={'fontsize':12},
        wedgeprops={'edgecolor':'black','linewidth':3},
        startangle=90)
plt.title("Students Marks Distribution")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()