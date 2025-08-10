# Define a class named Student
class Student:
    # Constructor method that accepts a variable number of arguments using *info
    def __init__(self, *info):
        if len(info) == 3:  # If 3 arguments are passed (name, id, CGPA)
            self.name = info[0]
            self.id = info[1]
            self.CGPA = info[2]
        elif len(info) == 2:  # If 2 arguments are passed (name, id)
            self.name = info[0]
            self.id = info[1]
            self.CGPA = None  # CGPA is not provided
        elif len(info) == 1:  # If only 1 argument is passed (name)
            self.name = info[0]
            self.id = None
            self.CGPA = None
        else:  # If no arguments are passed
            self.name = None
            self.id = None
            self.CGPA = None
        print("A student object created")  # Message shown when an object is created

# Creating student objects with different numbers of arguments
s1 = Student("shanto", 33, 3.80)  # All three values provided
s2 = Student("shimul", 34)        # CGPA not provided
s3 = Student("riyad")             # Only name provided
s4 = Student()                    # No information provided
