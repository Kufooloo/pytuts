#
# Example file for working with classes
#
class MyClass():
 def method1(self):
  print("MyClass","Method1")
 def method2(self, somestring):
  print("myClass method2"+somestring)
class anotherClass(MyClass):
 def method2(self):
  print("anotherClass Method2")
 def method1():
  MyClass.method1(self)
  print("anotherClass Method1")

def main():
 c = MyClass()
 # u = anotherClass()
 c.method1()
 c.method2(" nice")
 c.method1()
 u = anotherClass()
 u.method2()

 
 
  
if __name__ == "__main__":
  main()
