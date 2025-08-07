class student:
   def __init__(self,name,id):
     self.name=name #instance variable
     self.id=id    #instance variable
     print("a student object created")
     
s1=student("shanto",23)
s2=student("shimul",24)
s1.id=24 
print(s1.id)  