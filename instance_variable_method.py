class House:
  def __init__(self):
    self.window=4
    self.door=2
  def view(self):
    print(self.window,"windows",self.door,"door")
h1=House()
h2=House()
h1.window=6
h2.door=3
h1.view()
h2.view()
