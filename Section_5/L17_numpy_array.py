import numpy as np

my_list = [1,2,3]
arr = np.array(my_list) # Casting my_list as a NumPy array


# Two dimension array
my_mat = [[1,2,3], [4,5,6], [7,8,9]]
mat = np.array(my_mat) # Casting a 2D array into a NumPy array
print(mat)

#       arange
# Return evenly spaced values within a given interval.

arr = np.arange(0,10,2) # creates an array from 0 to <10 by step of 2


#       zeros and ones
# Generate arrays of zeros or ones

arr = np.zeros(3)     # 1D array of zeros
arr = np.zeros((2,3)) # 2,3 array  of zeros


#       linspace
# Return evenly spaced numbers over a specified interval.

arr = np.linspace(0,5,10)


#           eye
#   Create an identity matrix
arr = np.eye(4) # 4 is the dimesion of the identity matrix.

#
#           Random
# Numpy also has lots of ways to create random number arrays:

#            rand
# Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
np.random.rand(5)   # array of 5 random numbers
np.random.rand(3, 5)# array of 3, 5 random numbers

# randint
# Return random integers from low (inclusive) to high (exclusive).
np.random.randint(1,100)
np.random.randint(1,100,10)
