class Student:
    def __init__(self, name, id):
        self.__name = name   # Private attribute for name
        self.__id = id       # Private attribute for ID

    def details(self):
        # Print student's name and ID
        print("Name:", self.__name, "id:", self.__id)

    def set_name(self, name):
        # Update the name
        self.__name = name

    def get_name(self):
        # Return the private name attribute
        return self.__name

    def set_id(self, id):
        # Update the ID only if it is positive
        if id > 0:
            self.__id = id
        else:
            print("Invalid id, Enter id again")

    def get_id(self):
        # Return the private ID attribute
        return self.__id


# Create objects
s1 = Student("Shanto", 22)
s2 = Student("shimul", 33)

# Update values
s1.set_id(44)
s1.set_name("Aditto")
s2.set_id(55)
s2.set_name("Aronno")

# Show details
s1.details()
s2.details()
