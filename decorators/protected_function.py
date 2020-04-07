def protected(func):
    def wrapper(password):
        if password == 'wansoft':
            return func()
        else:
            print('Your password is wrong')

    return wrapper

@protected
def protected_func(password):
    print('Your password is OK')

if __name__ == '__main__':
    password = input('Type your password')
    protected_func(password)