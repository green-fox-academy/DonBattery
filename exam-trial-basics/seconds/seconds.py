def seconds(change_this):
    temp_list = []
    if len(change_this) > 1:
        for i in range(1,len(change_this)):
            if i % 2 != 0:
                temp_list.append(change_this[i])
    return temp_list
    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]

print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]
