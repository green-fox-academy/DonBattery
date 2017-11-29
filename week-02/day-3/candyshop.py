shop_items = ["Cupcake", 2, "Brownie", False]

# Accidentally we added "2" and "false" to the list. 
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)

for i in range(int(len(shop_items))):
    if shop_items[i] == 2:
        shop_items[i] = False
    elif shop_items[i] == False:
        shop_items[i] = 'Ice cream'

print(shop_items)