KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def encrypt(message):
    words = message.split(' ')
    encrypt_message = []
    for word in words:
        encrypt_word = ''
        for letter in word:
            encrypt_word += KEYS[letter]
        encrypt_message.append(encrypt_word)
    
    return ' '.join(encrypt_message) #join() is wonderfull

def decrypt(message):
    words = message.split(' ')
    decrypted_message = []
    for word in words:
        decrypted_word = ''
        for letter in word:
            for key, value in KEYS.items():
                if value == letter:
                    decrypted_word += key
                    break
        decrypted_message.append(decrypted_word)
    
    return ' '.join(decrypted_message)

def run():
    while True:
        command = input('''//////////////////////////////////////////////////////////////////
        Welcome to cryptography. What do you want to do?
        [e] encrypt message
        [d] decrypt message
        [x] exit
        ''')
        if command == 'e':
            message = input('Type your message')
            encrypt_message = encrypt(message)
            print(encrypt_message)
        elif command == 'd':
            message = input('Tyoe your encrypted message')
            decrypted_message = decrypt(message)
            print(decrypted_message)
        elif command == 'x':
            break
        else:
            print('invalid command!!')


if __name__ == '__main__':
    run()