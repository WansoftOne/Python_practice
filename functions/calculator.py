
def run():
    print('-----------COINS CALCULATOR-------------')
    print('Conver mexican coins to colombian coins.')
    print('')
    
    amount = float(input('type the amount of Mexican Coins that you want to convert'))
    result = foreign_exchange_calculator(amount)
    print('${} mexican coins is equals to ${}'.format(amount, result))
    print('')

def foreign_exchange_calculator(amount):
    mex_to_col_rate = 145.97
    return mex_to_col_rate * amount

def never():
    print("I never executed")

if __name__ == '__main__':
    run()