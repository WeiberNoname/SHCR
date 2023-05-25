# example.py
import ctypes

# Load the shared library
example = ctypes.CDLL('./example.so')

# Declare the function signature
example.calculateFactorial.argtypes = (ctypes.c_int64,)
example.calculateFactorial.restype = ctypes.c_int64

# Call the C++ function 
n = 5
result = example.calculateFactorial(n)
print(f"The factorial of {n} is: {result}")



