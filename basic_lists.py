list_x = [1, 2, 3]
list_y = list_x
print(list_x)
list_y[1]="Changed!"
print(list_x)
del list_y[-1]
print(list_x)
