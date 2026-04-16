import numpy as np

list1 = np.array([[10,20,50,70,70,80,80],[10,20,50,70,70,80,80]])

list2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

list3 = np.array([[[1,2,3],
                 [4,5,6],
                 [7,8,9]],[[1,2,3],
                 [4,5,6],
                 [7,8,9]]])

print(list1)
print(list1.shape)  # number of elements
print(list1.ndim)   # know the dimension of array


print(list2)
print(list2.shape)  # number of elements
print(list2.ndim)   # know the dimension of array

print(list3)
print(list3.shape)  # number of elements
print(list3.ndim)   # know the dimension of array
