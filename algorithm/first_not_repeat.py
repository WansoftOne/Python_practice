def first_not_repeating_char(char_sequence):
    chars = tuple(char_sequence)
    for char in chars:
        if char_sequence.count(char) == 1:
            return char
    return '_'

def first_not_repeating_char2(char_sequence):
    seen_letters = {}
    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)
    
    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append((key, value[0]))

    not_repeated_letters = sorted(final_letters, key = lambda value: value[1])
    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'

if __name__ == '__main__':
    char_sequence = input('Type a char sequence')
    result = first_not_repeating_char2(char_sequence)
    if result == '_':
        print('All chars are repeated')
    else:
        print('the first repeated char is {}'.format(result))

