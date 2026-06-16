class Dog:
  def __init__(self,name=""):
    self.name = ""
  def __str__(self):
    return self.name
  def bark(self):
    print (self.name,"says 'woof'!")  

Fido = Dog("Fido")
Spot = Dog("Spot")
print(type(Fido))
print(type(Spot))

Fido.bark()
Spot.bark()

print(Spot)

print((5).bit_length)