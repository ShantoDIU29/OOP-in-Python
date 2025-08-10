# Import the dispatch decorator from multipledispatch
from multipledispatch import dispatch

# Define a class named my_calculator
class my_calculator:

  # Overloaded method: product with two integer parameters
  @dispatch(int, int)
  def product(self, a, b):
    print(a * b)  # Prints the product of a and b

  # Overloaded method: product with three integer parameters
  @dispatch(int, int, int)
  def product(self, a, b, c):
    print(a * b * c)  # Prints the product of a, b, and c

# Create an object of the class
c1 = my_calculator()

# Call the product method with two arguments
c1.product(4, 5)       # Output: 20

# Call the product method with three arguments
c1.product(4, 5, 6)    # Output: 120
