class Dog:
  def __init__(self, name = ""):
    self.name = ""
  def bark(self):
    print (self.name,"says 'woof'!")  

fido = Dog("Fido")
Spot = Dog("")
print(type(fido))
print(type(spot))

fido.bark()
spot.bark()


print(spot)