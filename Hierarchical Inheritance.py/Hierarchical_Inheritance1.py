class Student:
  def __init__(self,name,id):
    self.name=name 
    self.id=id
  def details(self):
    print("Name:",self.name,"id:",self.id)  
class CSEStudent(Student):
  def __init__(self, name, id,labs):
    super().__init__(name, id)    
    self.no_of_labs=labs
    
  def cry(self):
    print("CSE student is crying because of",self.no_of_labs,"labs")
class BBAStudent(Student):
  def party(self):
    print("All day party")
    
s1=CSEStudent("Bob",22,3)
s2=BBAStudent("Carol",34)
s1.details()
s2.details()
s1.cry()
s2.party()   
print(help(s1))
print(help(s2))       #details documents show