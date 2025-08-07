class  student:
  def __init__(self,name,id):
    self.name=name
    self.id=id
  def s_details(self):
   print("name:",self.name,"id:",self.id)
s1=student("shanto roy",24)
s2=student("shimul mia",25)    
s3=student("Riyad",23)
s1.s_details() 
s2.s_details()
s3.s_details() 