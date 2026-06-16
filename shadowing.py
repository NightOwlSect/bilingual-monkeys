x = "a global variable!"
y = "a global variable!"

def my_func():
  global y
  x = "a shadowed variable!"
  y = "a non shadowed variable!"
  print ("x is", x)
  print ("y is", y)

print("x is", x)
print("y is", y)
my_func()
print("x is", x)
print("y is", y)
