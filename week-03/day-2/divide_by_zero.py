# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

def divider(Nnumber):    
    try:
        result = 10 / Nnumber
        print(result)    
    except ZeroDivisionError:
        print('fail')

divider(0)

    