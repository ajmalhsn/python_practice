import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]
#plt.plot(x,y,color="red")

# plt.plot(x,y,color='orange',linestyle='--',marker='x') # linestyle "-","--",":"  marker = "o","x","*"
# plt.xlabel("X Axis")
# plt.ylabel("Y axis")
# plt.title("Line Plot")

# plt.show()

stds = ["Std1","Std2","Std3","Std4","Std5","Std6","Std7"]
marks = [40,50,80,90,80,70,70]
# plt.bar(stds,marks,color=["red","blue","green"],width=0.5,edgecolor='black')
bars = plt.bar(stds,marks,color=["red","blue","green"],edgecolor='black')
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height()+ 1,bar.get_height(),ha="center",va="center")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
