dictionary = {} #initilize MAP
dictionary['Matematiocas'] = 9
dictionary['English'] = 7
dictionary['IT'] = 8
dictionary['Web Development'] = 10

total = 0

for key in dictionary:
    print(key)

for value in dictionary.values():
    print(value)
    total += value

average = total / len(dictionary)
print('Your average is {}'.format(average))

for key, value in dictionary.items():
    print('key: {}, value:{}'.format(key,value))

