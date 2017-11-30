# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# OPTIONAL:
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True },
    { "name": "recsegvefingókecske mitsütszkisszűcs", "in_stock": 19999, "needs_cooling": False}
]

def table_printer(ttable):

    max_len = 10
    needcool = ''
    stockmark = ''

    for i in range(len(ttable)):
        if len(ttable[i]['name']) > max_len:
            max_len = len(ttable[i]['name'])
    
    print('+' + '-' * (max_len +2 ) + '+---------------+----------+')
    print('| Ingredient ' + ' ' * (max_len-10) + '| Needs cooling | In stock |')   

    for i in range(len(ttable)):
        if ttable[i]['needs_cooling']:
            needcool ='Yes'
        else:
            needcool = 'No '
        if ttable[i]['in_stock'] == 0:
            stockmark = '-        |'
        else:
            stockmark = (str(ttable[i]['in_stock']) + ' ' * (9 - len(str(ttable[i]['in_stock']))) + '|')            
        print('| ' + ttable[i]['name'] + ' ' * (max_len - len(ttable[i]['name']) + 1) + '| ' + needcool + '           | ' + stockmark)
    
    print('+' + '-' * (max_len + 2) + '+---------------+----------+')

table_printer(ingredients)
