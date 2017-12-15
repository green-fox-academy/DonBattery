pirates = [
    {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
    {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
    {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
    {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
    {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that
# - have wooden leg and
# - have more than 15 gold

def pirate_counter(input_list):
    output_list = []
    for i in range(len(input_list)):
        if input_list[i]['has_wooden_leg'] and input_list[i]['gold'] > 15:
            output_list.append(input_list[i])
    return output_list

print(pirate_counter(pirates))
