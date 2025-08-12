class student:
    def __init__(self, name, id):
        self.name = name        # Public attribute
        self.__id = id          # Private attribute

    def details(self):
        # Public method to print details
        print("Name:", self.name, "id:", self.__id)  
        self.__method()  # Calling the private method from inside the class

    def __method(self):
        # Private method
        print("Private method executed")


# Creating objects
s1 = student("Shanto", 33)
s2 = student("additto", 44)

# ❌ This will give an error because __method is private:
# s1.__method()

# ✅ But calling details() works because it calls __method() internally
s1.details()
