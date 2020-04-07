def palindromeTwo(word):
    reversed_letters = []
    for letter in word:
        reversed_letters.insert(0, letter)
    
    reversed_word = ''.join(reversed_letters)
    if reversed_word == word:
        return True
    else:
        return False

def palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

if __name__ == '__main__':
    word = input('Type a word')
    is_palindrome = palindrome(word)
    if is_palindrome is True :    
        print('{} is a palindrome'.format(word))
    else:
        print('{} isn\' palindrome'.format(word))

