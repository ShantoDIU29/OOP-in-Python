# class phone:
#   manufactured='china'
#   def send_sms(self,phone,sms):
#     text=f'sending to:{phone}{sms}'
#     print(text)
class Employee:
  def __init__(self,name,id):
    self.no=id
    self.name=name
  def display(self):
    print(self.name,self.no)
emp1=Employee('shanto',23)
emp2=Employee('shimul',24)
emp1.display()
emp2.display()      
    