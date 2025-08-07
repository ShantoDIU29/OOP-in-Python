class Dog:
  def __init__(self,name,color):
    self.name=name
    self.color=color
    
  def update_color(self,color,name):
    self.color=color
    self.name=name
  def poke(self):
    print(self.color,self.name,"is smiling")     
d1=Dog("rover","brown")
d2=Dog("tomy","white")
d1.poke()
d1.update_color("tony","black")
d1.poke()
d2.poke()
d2.update_color("billu","red")
d2.poke()    
# print(d1.__dict__)#built in method
# print(d2.__dict__)
print(dir(d1  ))