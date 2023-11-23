# Basic Operations


import numpy


numpy.array()               # Create an array.
numpy.arange()              # Return evenly spaced values within a given interval.
numpy.linspace()            # Return evenly spaced numbers over a specified range.
numpy.zeros()               # Return a new array of given shape and type, filled with zeros.
numpy.ones()                # Return a new array of given shape and type, filled with ones.
numpy.eye()                 # Return a 2-D array with ones on the diagonal and zeros elsewhere.
numpy.random.rand()         # Generate random numbers in [0, 1) uniform distribution.
numpy.random.randn()        # Generate random samples from the standard normal distribution.
numpy.reshape()             # Reshape an array.
numpy.concatenate()         # Join arrays along an existing axis.
numpy.split()               # Split an array into multiple sub-arrays.
numpy.unique()              # Find unique elements in an array.

# Array Manipulation
numpy.transpose()           # Reverse or permute the axes of an array.
numpy.vstack()              # Stack arrays in sequence vertically.
numpy.hstack()              # Stack arrays in sequence horizontally.
numpy.flatten()             # Return a copy of the array collapsed into one dimension.
numpy.append()              # Append values to the end of an array.
numpy.delete()              # Return a new array with sub-arrays along an axis deleted.

# Mathematical Operations
numpy.sum()                 # Sum of array elements along a specified axis.
numpy.mean()                # Compute the arithmetic mean along the specified axis.
numpy.median()              # Compute the median along the specified axis.
numpy.std()                 # Compute the standard deviation along the specified axis.
numpy.min()                 # Return the minimum value along an axis.
numpy.max()                 # Return the maximum value along an axis.
numpy.argmin()              # Return the indices of the minimum values along an axis.
numpy.argmax()              # Return the indices of the maximum values along an axis.
numpy.sin()                 # Trigonometric sine, element-wise.
numpy.cos()                 # Trigonometric cosine, element-wise.
numpy.exp()                 # Calculate the exponential of all elements in the input array.

# Linear Algebra
numpy.dot()                 # Dot product of two arrays.
numpy.linalg.inv()          # Compute the (multiplicative) inverse of a matrix.
numpy.linalg.det()          # Compute the determinant of an array.
numpy.linalg.eig()          # Compute the eigenvalues and right eigenvectors of a square array.

# Statistics
numpy.percentile()          # Compute the q-th percentile of the data along the specified axis.
numpy.histogram()           # Compute the histogram of a set of data.
numpy.correlate()           # Compute the cross-correlation of two 1-dimensional sequences.

# Indexing and Slicing
numpy.where()               # Return elements chosen from x or y depending on condition.
numpy.argwhere()            # Find the indices of array elements that are non-zero.
numpy.take()                # Return elements at indices along a given axis.
numpy.choose()              # Construct an array from an index array and a set of arrays to choose from.

# Trigonometric Functions
numpy.arcsin()              # Inverse sine, element-wise.
numpy.arccos()              # Inverse cosine, element-wise.
numpy.arctan()              # Inverse tangent, element-wise.





#######################################  Numpy Array methods  ###############################





# Creation
numpy.array()           # Create an array from a list or tuple.
numpy.arange()          # Return an array with evenly spaced values within a given interval.
numpy.linspace()        # Return an array with evenly spaced numbers over a specified range.
numpy.zeros()           # Return an array filled with zeros.
numpy.ones()            # Return an array filled with ones.
numpy.eye()             # Return a 2-D array with ones on the diagonal and zeros elsewhere.
numpy.empty()           # Return a new array without initializing entries.

# Inspection
numpy.shape()           # Return the shape of an array.
numpy.ndim()            # Return the number of dimensions of an array.
numpy.size()            # Return the number of elements in an array.
numpy.dtype()           # Return the data type of an array.
numpy.itemsize()        # Return the size of one array element in bytes.

# Reshaping
numpy.reshape()         # Reshape an array.
numpy.resize()          # Return a new array with a specified shape.
numpy.flatten()         # Return a copy of the array collapsed into one dimension.
numpy.ravel()           # Return a flattened array.

# Stack and Split
numpy.vstack()          # Stack arrays vertically.
numpy.hstack()          # Stack arrays horizontally.
numpy.split()           # Split an array into multiple sub-arrays.
numpy.hsplit()          # Split an array horizontally.
numpy.vsplit()          # Split an array vertically.

# Indexing and Slicing
numpy.index()           # Return an index along a specified axis.
numpy.s_()              # Build an index expression for NumPy array slicing.
numpy.take()            # Return elements at specified indices along a given axis.
numpy.choose()          # Construct an array from an index array and a set of arrays to choose from.

# Mathematical Operations
numpy.sum()             # Sum of array elements along a specified axis.
numpy.mean()            # Compute the mean of array elements along a specified axis.
numpy.median()          # Compute the median along the specified axis.
numpy.std()             # Compute the standard deviation along the specified axis.
numpy.min()             # Return the minimum value along an axis.
numpy.max()             # Return the maximum value along an axis.
numpy.argmin()          # Return the indices of the minimum values along an axis.
numpy.argmax()          # Return the indices of the maximum values along an axis.

# Mathematical Functions
numpy.sin()             # Trigonometric sine, element-wise.
numpy.cos()             # Trigonometric cosine, element-wise.
numpy.exp()             # Calculate the exponential of all elements in the input array.
numpy.sqrt()            # Return the non-negative square root of an array.

# Linear Algebra
numpy.dot()             # Dot product of two arrays.
numpy.cross()           # Return the cross product of two (arrays of) vectors.

# Random
numpy.random.rand()     # Generate random numbers in [0, 1) uniform distribution.
numpy.random.randn()    # Generate random samples from the standard normal distribution.
numpy.random.choice()   # Generate a random sample from a given 1-D array.
numpy.random.shuffle()  # Shuffle the contents of an array in place.
