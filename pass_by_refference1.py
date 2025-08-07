class Cat:
  def __init__(self,color,action):
    self.color=color
    self.action=action
  def view(self):
       print(self.color,"cat is",self.action)
  def compare(self,ct):#here c is reference
    if self.action==ct.action:
         print("both cats are",self.action)
    else:
      print("they are different")       
#================================================
c1=Cat("white","jumping")
c2=Cat("brown","siting")
c1.view()
c2.view()
c1.compare(c2)
