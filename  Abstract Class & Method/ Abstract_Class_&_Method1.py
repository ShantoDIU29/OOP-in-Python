from abc import ABC,abstractmethod
class A(ABC):
  @abstractmethod
  def method1(self):
    pass
class B(A):
    def method1(self):
      print("Method1 is overriden")
b=B()
b.method1()      
      