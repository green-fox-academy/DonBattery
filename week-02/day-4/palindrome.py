
input1 = input('Kérem a palindrómásítandó kifejezést : ')

def create_palindrome(word):
    chars = []
    rev = []
    pali = word

    for i in range(len(pali)):
        chars.append(pali[i])
    
    rev = chars[:]

    rev.reverse()
    
    for i in range(len(rev)):
        if chars[i] != rev[i]:
            for j in range(len(pali)):
                chars.append(pali[len(pali)-j-1])
            pali = ''
            for j in range(len(chars)):
                pali += chars[j]
            return pali
    return pali

print('Az ön palindrómája : ', create_palindrome(input1))