class my_calculator:
  def product(self,num1=None,num2=None,num3=None):
    if num1!=None and num2!=None and num3!=None:
     print(num1*num2*num3)
    elif num1!=None and num2!=None:
      print(num1*num2) 
    else:
      print(1*num1)  

#method holo kno class same name method defferent paramter atai    
#=======================
c1=my_calculator()
c1.product(4,5)
c1.product(4,5,6)
c1.product(4)
c1.product(4,5,6,7)