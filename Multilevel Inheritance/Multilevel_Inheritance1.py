class student:
  def __init__(self,name,id):
    self.name=name
    self.id=id
  def details(self):
    print("Name:",self.name,"id:",self.id)
class CSEStudent(student):
   def __init__(self, name, id,labs):
     super().__init__(name, id) 
     self.no_of_labs=labs   
   def cry(self):
     print(self.name,"is crying becasue of",self.no_of_labs,"labs") 
class CSEFresher(CSEStudent):
    def enroll_cse110(self):
      print("Enrolled in cse110")      
s1=CSEStudent("bob",22,3) 
s2=CSEFresher("carol",33,2)
s2.details()
s1.details()
s2.cry( )   