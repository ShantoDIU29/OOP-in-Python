class student:#class /design/blueprint
  def __init__(self,nm,id):  #constructor
    print("an object is created")
    self.name=nm 
    self.id=id
  def details(self):
    print(self.name,self.id)  

#variable=classname() this is object created    
s1=student("shanto",1) #1st object/instance
s2=student("shimul",2) #2nd object/instance
s1.details()
s2.details()