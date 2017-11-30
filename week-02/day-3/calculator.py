# Create a simple calculator application which does read the parameters from the prompt 
# and prints the result to the prompt. 

# It should support the following operations: 
# +, -, *, /, % and it should support two operands. 

# The format of the expressions must be: {operation} {operand} {operand}. 
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# print the result
# Exit

def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False

def first(sString = ''):
    i = 2
    numString = ''
    while (i < len(sString)) and (sString[i] != ' '):
        numString = numString + sString[i]
        i += 1
    return numString

def second(sString = ''):
    i =  + int(len(first(sString)))
    numString = ''
    while (i < len(sString)) and (sString[i] != ' '):
        numString = numString + sString[i]
        i += 1
    return numString
        
def check(cline = ""):
    if (cline.count(" ") == 2):
        print('Empty spaces checked OK')
    if (cline[0] in ["-","+","*","/","%"]):
        print('Operator is valid OK')
    if (cline[1] == ' '):
        print('First space in position 1 OK')
    if (int(len(cline)) >= 5): 
        print('Command is long enough OK')
    if (not(cline.endswith(' '))):
        print('Command does not end with " " OK')
    if isfloat(first(cline)):
        print('First number is float OK')
    if isfloat(second(cline)):
        print('Second number is float OK')
        
    if (cline.count(" ") == 2) and (cline[0] in ["-","+","*","/","%"]) and (cline[1] == ' ') and (int(len(cline)) >= 5) and (not(cline.endswith(' '))) and isfloat(first(cline)) and isfloat(second(cline)):
        return True
    else:
        return False

Good  = False

print("The magnificant calculator \n")

while not(Good):

    print("Usage: {operation} {operand} {operand} \n")
    command = input("Please type in the expression : ")
    if (command.count(" ") == 2):
        print('Empty spaces checked OK')
    else:
        print('Too many spaces in command')

    if (command[0] in ["-","+","*","/","%"]):
        print('Operator is valid OK')
    else:
        print('Invalid operator')

    if (command[1] == ' '):
        print('First space in position 1 OK')
    else:
        print('No space after operator')

    if (int(len(command)) >= 5): 
        print('Command is long enough OK')
    else:
        print('Invalid operator')
        
    if (not(command.endswith(' '))):
        print('Command does not end with " " OK')

    command = command.split(' ')

    if check(command):
        num1 = float(first())
        num2 = float(second())
        result = 0
        if command[0] == '+':
            result = num1 + num2
        elif command[0] == '-':
            result = num1 - num2
        elif command[0] == '*':
            result = num1 * num2
        elif command[0] == '/':
            result = num1 / num2
        elif command[0] == '%':
            result = num1 % num2
        print('\n' + 'The result of your operation is : ' + str(result))
        Good = True
    else:
        print('\n'+'Syntax error ...')
        num1 = first()
        num2 = second()
        print('Num1 is ', num1)
        print('Num2 is ', num2)

