class A:
    def __init__(self):
        print("__init__ of class A")   # Constructor of class A, prints a message when an object is created
    
    def method1(self):
        print("Always studey")          # A method in class A
    
    def mehtod2(self):
        print("you will get of my properties and method")  # Another method in class A
        
class B(A):
    def __init__(self):
        pass                             # B's constructor does nothing (overrides A's __init__)
        # print("__init__ of class B")   # This line is commented out, so nothing happens here
    
    def method1(self):
        print("Always party")             # B overrides method1 of A
        
b1 = B()                               # Create object of B
# Here, B.__init__ runs. It has 'pass', so nothing is printed.
b1.method1()                            # Calls B's method1 → prints "Always party"
b1.mehtod2()                            # Calls inherited method from A → prints "you will get of my properties and method"
