def average_temps(temps):
    sum_of_temps = 0
    for temp in temps:
        sum_of_temps += temp

    return sum_of_temps / len(temps)

if __name__ == '__main__':
    temps = [21,24,22,26,27,24,25]
    average = average_temps(temps)
    print('The average temperture is {}'.format(average))