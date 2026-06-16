shopping_list = []
action = ""
while action != "stop":
    elemnt = input("Type the object you want to add to the list: ")
    # add code to add the entered item here
    action = input("Type 'clear' to clear the list or 'stop' to stop entry: ")
    # add code to clear the list if the user typed clear here
    print(shopping_list)