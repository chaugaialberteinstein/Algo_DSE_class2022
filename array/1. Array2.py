import numpy as np

# Create
twoDArray = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print(twoDArray)

# Insert

# newTwoDArray = np.insert(twoDArray,1, [[1,2,3,4]], axis = 1)
# print(newTwoDArray)
# newTwoDArray = np.append(twoDArray,[[1,2,3,4]], axis = 0)
# print(newTwoDArray)

# Access an element of two dimensional array
# def accessElements(array, rowIndex, colIndex):
#     if rowIndex >= len(array) or colIndex >= len(array[0]):
#         print('Incorrect index')
#     else:
#         print(array[rowIndex][colIndex])
# accessElements(twoDArray,2,3)


# Traversal - Two Dimension Array
# def traversalTDArray(array):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             print(array[i][j])

# traversalDArray(twoDArray)

# Search 
# def searchTDArray(array,value):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if array[i][j] == value:
#                 return 'The value is located at index '+str(i)+" "+str(j)
#     return 'The element is not found'
    
# print(searchTDArray(twoDArray,7))



# Delete
# newTDArray = np.delete(twoDArray, 0, axis = 0) # O(mn)
# print(newTDArray)