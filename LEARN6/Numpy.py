import numpy as np
import datetime
##my_list = [1, 2, 3, 4]
#print(my_list)

#array = np.array([1, 2, 3, 5, 8])
#array = array * 2
#print(array)

# Multidemension arrays
array = np.array(['A', 'B', 'C']) # This is 1 demensional arrays
array = np.array([['A', 'B', 'C'], ['D', 'E', 'F']]) # This is 2 demensional arrays
print(array.ndim)

# Slicing
array = np.array ([[1, 2, 3, 4], 
                   [5, 6, 7, 8,], 
                   [9, 10, 11, 12], 
                   [13, 14, 15, 16]])
#array[start;end;step]
print(array[0:3]) # end
#print(array[1]) start
#print([0:2:4]) step

arr = np.array([1, 2, 3, 4, ], dtype='S')
print(arr)
print(arr.dtype)

#Arithemtic / Scalar
array = np.array ([1, 2, 4, 6])
print(array +2)
print(array -2)
print(array *4)
print(array /2)

# Vectorized math function
array = np.array ([2, 4, 6])
print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
# Execrise
radii = np.array([1,2,3])
print(np.pi * radii ** 2)

# Elemnet-wise arithematic
array1 = np.array([1,2,3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 ** array2)

# Camparison operators
scores = np.array([90, 65, 50, 100, 75])
print(scores ==100)
print(scores >=60)

scores = np.array([90, 65, 50, 100, 75])
scores[scores <60] = 0
print(scores)

# BROADCASTING IN NUMPY
array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)

# Aggregate Function
array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])
print(np.sum(array))
print(np.mean(array))
print(np.var(array))
print(np.std(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array)) 

# Filtering
ages = np.array([[13, 17, 40, 35, 18], 
                 [30, 22, 15, 19, 18,]])
teenagers = ages[ages < 18]
print(teenagers)
adults = ages[(ages >= 18) & (ages < 65)]
print(adults)
seniors = ages[ages >= 65]
print(seniors)

# Working with datetime
date = datetime.date(2025, 1, 26)
today = datetime.date.today()

print(today)

time = datetime.time(1, 30, 0)
print(time)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m-%d-%Y")
print(now)

# To check if a datetime is current or passed
target_datetime = datetime.datetime(2010, 1, 12, 4, 30, 10)
current_datetime = datetime.datetime.now()

if target_datetime > current_datetime:
    print("Target datetime has passed")
else:
    print("Target datetime has NOT passed")

arr = np.array([1, 2, 3, 4, ], dtype='S')
print(arr)
print(arr.dtype)
