# This file demonstrates the Factorial recursive function with
# a guardian that raises exceptions for bad input.

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer!")
    elif n < 0:
        raise ValueError("n cannot be negative!")

    
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(10))

try:
    factorial("nope")
except:
    print("Something bad happened with the factorial function")

# Try uncommenting the following code below to see the exception working
#print(factorial("nope"))
#print(factorial(-1))