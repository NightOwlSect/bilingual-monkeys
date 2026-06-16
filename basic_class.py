class Dog:
  pass

fido = Dog()
spot = Dog()
print(type(fido))
print(type(spot))

fido.name = "Fido"
print(fido.name)

new_dog= spot
new_dog.name = "New dog"
print(spot.name)

print(spot)