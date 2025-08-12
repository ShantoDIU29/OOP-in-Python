class student:
  counter=0   #class or static variable
  def __init__(self,name,id):
    self.name=name
    self.id=id
    student.counter+=1
    
  def details(self):
     print("name:",self.name,"id:",self.id,"student counter",student.counter)
     
print("student count",student.counter)
s1=student("shanto",44)
s2=student("shimul",33)
s3=student("riyad",45)
s2.details()
s1.details()
s3.details()