x = "Variable x exists"
print(x, "outside of a function!")

def my_func():
  print(x, "inside a function!")
  y = "Variable y exists!"
  print(y, "inside a function!")

my_func()
print(y, "outside of a function!")
