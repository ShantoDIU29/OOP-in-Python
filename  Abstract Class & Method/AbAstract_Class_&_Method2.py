from abc import ABC, abstractmethod   # ABC = Abstract Base Class, abstractmethod = decorator for abstract methods

class A(ABC):   # Abstract class A
  @abstractmethod
  def method1(self):   # Abstract method (no implementation)
    pass

class B(A):   # Class B inherits from A
  @abstractmethod
  def method1(self):# Still abstract (so B is also abstract)
      pass

class C(B):# Class C inherits from B
   def method1(self):# Overriding abstract method (now implemented)
     print("Method1 is overriding")
   def method2(self):# A new normal method
     print("Method2 is overriding")    

c = C()# Object creation of class C (possible because C is not abstract anymore)
c.method1()# Calls overridden method1 → Output: Method1 is overriding
c.method2()# Calls method2 → Output: Method2 is overriding
