def ifplaindrome(sstring):
    
    chars = []

    for i in range(len(sstring)):
        chars.append(sstring[i])
    
    rev = chars[:]
    rev.reverse()
    
    for i in range(len(rev)):
        if chars[i] != rev[i]:
            return False
    return True

def find_plaindromes(sstring):

    if len(sstring) < 3:
        return 'Túl rövid szöveget adott meg.'

    palindromes = []

    for i in range(len(sstring)-2):
        for j in range(i+2, len(sstring)+1):
            if ifplaindrome(sstring[i:j]):
                palindromes.append(sstring[i:j])
    
    if len(palindromes) == 0:
        return 'Nincsenek palindrómák a szövegben'
    return palindromes

word = input('Kérek egy szöveget : ')

print(find_plaindromes(word))