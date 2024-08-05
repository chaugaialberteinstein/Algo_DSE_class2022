# Create an array
# import array

# my_array = array.array('i')
# print(my_array)

# my_array1 = array.array('i',[1,2,3,4])
# print(my_array1)

# import numpy as np
# np_array = np.array([], dtype=int)
# print(np_array)

# np_array1 = np.array([1,2,3,4])
# print(np_array1)

# Insert to array
# import array

# my_array1 = array.array('i',[1,2,3,4])
# print(my_array1)
# my_array1.insert(5,6)
# print(my_array1)



# Array traversal
# from array import *
# arr1 = array('i',[1,2,3,4,5,6])
# arr2 = array('d',[1.3,1.5,1.6])

# def traverseArray(array):
#     for i in array:
#         print(i)
# traverseArray(arr1)



# Access array element
# from array import *
# arr1 = array('i',[1,2,3,4,5,6])

# def accessElement(array,index):
#     if index >= len(array):
#         print('There is not any element in this index')
#     else:
#         print(array[index])

# accessElement(arr1,2)


# Linear Search
# import array
# my_array1 = array.array('i',[1,2,3,4,5])

# def linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
#         return -1
# print(linear_search(my_array1,8))


# Delete an element from array
# from array import *
# arr1 = array('i',[1,2,3,4,5,6])
# arr1.remove(6) # O(n)
# print(arr1)



