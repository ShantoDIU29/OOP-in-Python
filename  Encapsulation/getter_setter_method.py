class Student:
    def __init__(self, name, id):
        self.name = name        # Public attribute
        self.__id = id          # Private attribute (can only be accessed inside the class)
    def details(self):
        # Print student's name and ID
        print("Name:", self.name, "id:", self.__id)
    def set_id(self, id):
        # Set a new ID after validation
        if id > 0:
            self.__id = id
        else:
            print("Invalid id, enter id again")
    def get_id(self):
        # Return the private attribute __id
        return self.__id  
# Creating objects
s1 = Student("shanto", 22)
s2 = Student("shimul", 24) 
s3 = Student("Riyad", 33) 
# Update ID
s1.set_id(55)
# Display ID
print(s1.get_id())
