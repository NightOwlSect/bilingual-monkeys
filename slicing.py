my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)
print(my_list[2:5])
new_list = my_list[-5:-2]
print(new_list)
my_list[-5:-2] = [0]
print(my_list)
print(new_list)
