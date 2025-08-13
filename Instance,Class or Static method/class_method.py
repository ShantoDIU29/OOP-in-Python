class Student:
     uni_name="DIU"
     def __init__(self,name,id):
       self.name=name
       self.__id=id
       
     def details(self):
         print("Name:",self.name,"id:",self.__id,Student.uni_name)
     @classmethod
     def update_uni_name(cls,u_name):
       cls.uni_name=u_name               
     
s1=Student("shanto",34)
s2=Student("Shimul",44)
s1.details()
s2.details()
Student.update_uni_name("DHAKA INTERNATIONAL UNIVERSITY") 
s1.details()
s2.details()    
     