class Book:
   def __init__(self,name,author):
     self.name=name  #instance variable
     self.author=author #instance variable
     self.price=0      #instance variable
   def set_price(self,price):#update price
     self.price=price
   def  get_price(self): #update show 
      return self.price
   def details(self):
     print("Book Name:",self.name,"\nAuthor:",self.author,"\nPrice :",self.price,"taka")
d1=Book("Opekkha","Humayun Ahmed") 
d1.details()
d1.set_price(255)
d1.get_price()
# print(x)
d1.details()
#if another folder run when 
# import constructor_instance_importclass

# d1=constructor_instance_importclass.Book("Opekkha","Humayun Ahmed") 
# d1.details()
# d1.set_price(255)
# d1.get_price()
# # print(x)
# d1.details()
  
     
       
      