# n1=10
# n2=20
# print(n1+n2)
# print(n1.__add__(n2))
class data:
  def __init__(self,x):
    self.x=x
  def __add__(self,other): 
    return self.x+other.x 
num1=data(10)
num2=data(20)
str1=data("cse")
str2=data("111")
print(num1+num2)