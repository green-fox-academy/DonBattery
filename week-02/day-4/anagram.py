
input1 = input('Kérem az első szót : ')
input2 = input('Kérem a második szót : ')

def check_anagram(word1, word2):
    char_list_1 = []
    char_list_2 = []

    for i in range(len(word1)):
        char_list_1.append(word1[i])
    
    for i in range(len(word2)):
        char_list_2.append(word2[i])

    char_list_1.sort()
    
    char_list_2.sort()

    if char_list_1 == char_list_2:
        return True
    else:
        return False 

if check_anagram(input1, input2):
    print('A két szó egymás anagrammája')
else:
    print('A két szó nem egymás anagrammája')
