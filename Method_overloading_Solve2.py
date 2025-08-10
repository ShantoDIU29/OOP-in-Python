# Define a class named my_calculator
class my_calculator:
  
  # Define a method 'product' that accepts any number of arguments using *nums
  def product(self, *nums):
    product = 1  # Initialize product to 1
    print(nums)  # Print the tuple of input numbers
    for x in nums:  # Loop through each number in the tuple
       product = product * x  # Multiply each number with the product
    print(product)  # Print the final product


# Create an object of the class
c1 = my_calculator()

# Call the product method with different numbers of arguments
c1.product(4)             # Output: (4), then 4
c1.product(4, 5)          # Output: (4, 5), then 20
c1.product(4, 5, 6)       # Output: (4, 5, 6), then 120
c1.product(4, 5, 6, 7, 8) # Output: (4, 5, 6, 7, 8), then 6720

# Note:
# Python does not support traditional method overloading (same method name with different parameters).
# Instead, using *args (like *nums here) allows you to pass a variable number of arguments to a method.
