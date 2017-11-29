# Create a function called 'reverse_string' which takes a string as a parameter
# The function reverses it and returns with the reversed string


reversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"

def reverse(StringA=""):
    StringB = ""
    for i in range(int(len(StringA))):
        StringB = StringB + StringA[int(len(StringA)) - i - 1]
    return StringB

print(reverse(reversed))
