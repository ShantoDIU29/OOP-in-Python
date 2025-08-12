class Student:
  def __init__(self,name,id):
    self.name=name #instance variable
    self.__id=id  #(__)private instance variable 
  
  def details(self): #instance method
    print("Name:",self.name,"ID:",self.__id)  
  def update_Id(self,ID):
     if(ID>0):
       self.__id=ID
     else:
       print("Invalid ID,enter id again")    
s1=Student("Shanto",11)
s2=Student("shimul",24)
s1.__id=-66    
print(s1.__dict__)  #{'name': 'Shanto', '_Student__id': 11, '__id': -66}
s1.update_Id(66)
s1.details()
s2.details()    
    