#import lamp #Import one module
from lamp import Lamp #import one class

def run():
    #lamp1 = lamp.Lamp(is_turned_on=False)
    lamp1 = Lamp(is_turned_on=False)
    while True:
        command = input('''
            What so you want to do?
            [1] Turn ON
            [0] Turn OFF
            [3] Exit
        ''')
        if command == '1':
            lamp1.turn_on()
            lamp1._display_image()
        elif command == '0':
            lamp1.turn_off()
        else:
            break

if __name__ == '__main__':
    run()
