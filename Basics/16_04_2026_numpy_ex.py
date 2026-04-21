import numpy as np


# list1 = np.array([[10,20,50,70,70,80,80],[10,20,50,70,70,80,80]])

# list1 = np.array([[10,20,50,70,70,80,80],[10,20,50,70,70,80,80]])
# print(list1.shape)
# print(list1.ndim)
# list2 = np.array([[1,2,3],
#                  [4,5,6],
#                  [7,8,9]])

# list3 = np.array([[[1,2,3],
#                  [4,5,6],
#                  [7,8,9]],[[1,2,3],
#                  [4,5,6],
#                  [7,8,9]]])

# print(list1)
# print(list1.shape)  # number of elements
# print(list1.ndim)   # know the dimension of array


# print(list2)
# print(list2.shape)  # number of elements
# print(list2.ndim)   # know the dimension of array
# print(list2.dtype)   # know the datatype of array

# print(list3)
# print(list3.shape)  # number of elements
# print(list3.ndim)   # know the dimension of array

# # Example 2
# print(np.zeros((2,3))) # creates an array of zeroes of 2 * 3 matrix
# print(np.ones((2,3))) # creates an array of ones of 2 * 3 matrix
# print(np.eye(3)) # creates an identity matrix of 3 * 3
# print(np.arange(0,10,2)) # creates an array of matrix with increment in two till 10 but 10 is excluded
# print(np.linspace(0,1,5)) # divides the array into 5 parts between 0 & 1 with 1 not included

# # Example - 3
# list1 = np.array([10,20,30,40,50])
# print(list1[0]) # 10
# print(list1[-5]) #10
# print(list1[1:3]) # 1 will include and 3 will exclude
# print(list1[1:]) # 1 to end [20,30,40,50]
# print(list1[:3]) # 0 will include and 3 will exclude [10,20,30]

# Example - 4
# list2 = np.array([[1,2,3],
#                   [4,5,6]])

# print(list2[0][0])
# print(list2[1][2])
# print(list2[:,0]) # col1
# print(list2[:,1]) # col2
# print(list2[:,2]) # col3

# print(list2[0]) # row1
# print(list2[1]) # row2

# Example 5

# list1 = np.array([[1,2,3],
#                   [4,5,6],
#                   [7,8,9]])

# print(list1[:,0]) # 1 col
# print(list1[:,0:2]) # first two columns
# print(list1[0:2]) # first two rows 

# # Example 6
# # Vectorization
# # 
# print("Example 6")
# list1 = np.array([1,2,3])
# print(list1 + 2)
# print(list1 * 2)
# print(list1 - 2)
# print(list1 / 2)
# print(list1 ** 2)

# list1 = np.array([1,2,3,4,5])
# print(f'min element {np.min(list1)}')
# print(f'max element {np.max(list1)}')
# print(f'sum element {np.sum(list1)}')
# print(f'mean elements {np.mean(list1)}')
# print(f'sqrt element {np.sqrt(list1)}')
# print(f'median elements {np.median(list1)}')

# # Example 8
# list1 = np.array([1,2,3])
# list2 = np.array([[10],[20],[30]])
# print(list1 + list2)

# print("Print Tuple: {}", (5))

# Example-9
list1 = np.array([[1,2],
                  [3,4]])
list2 = np.array([[5,6],
                  [7,8]])

print(np.dot(list1,list2)) # multiplication of matrix
"""
0,0 * 0,0 + 0,1 * 1,0  ,   0,0 * 1,0 + 1,0 * 1,1

0,0 * 0,1 + 1,1 * 1,0  ,   
"""

# Example - 10
# 0 10 100 42 official numbers given by python
# this numbers are some special numbers in the number system 

# np.random.seed(42)
# print(np.random.rand(2,2))
# print(np.random.randint(1,10,(2,3)))
# print(np.random.rand(3))

# print(np.full((3,3),100))


# list1 = np.array([10, 20, 30, 40, 50])
# print(list1[list1>30])
# print(list1[list1<30])

# list1 = np.array([[1,2,3],
#                  [4,5,6]])

# print(np.sum(list1,axis=0))  # Column-wise sum 
# print(np.sum(list1,axis=1))  # row-wise sum

# list = np.arange(6)

# print(list)
# print(list.reshape(2,3)) # convert 1D to Multi Dimension
# list3 = list.flatten() # convert Multi Dimension to 1D
# print(list3)

# list1 = np.array([1,2])
# print(list1.reshape(-1, 1))

# Example 11

# list1 = np.array([2, 1])
# list2 = np.array([6, 5])

# print(np.vstack((list1, list2)))
# print(np.hstack((list1, list2)))

# Example 12
list4 = np.array([1,2,3,4,5,6])
new_list = np.split(list4,2)

print(new_list[1])

# list1 = np.array([1,2,3])
# list2 = list1  # ref copy
# list1[0] = 1000
# print(list1)
# print(list2)

list1 = np.array([1, 2, 3])
list2 = list1.copy()
list1[0] = 1000
print(list1)
print(list2)

list1 = np.array([3,1,4,2])
print(np.sort(list1)) # elements of the array after sorting
print(np.argsort(list1)) # indexes of the array before sorting


list1 = np.array([[1,2],[3,4]])
list2 = np.array([[5,6],[7,8]])

new_list1 = np.dot(list1, list2)
print(new_list1)
print(new_list1.T)
print((new_list1.T).T)