import random

def run():
    number_found = False
    random_number = random.randint(0,20)
    while not number_found:
        number = int(input('Try a number: '))
        if number == random_number:
            print ('Congratulations, You found the number')
            number_found = True
        elif number > random_number:
            print('The number is smaller')
        else:
            print('The number is bigger')
            
if __name__ == '__main__':
    run()