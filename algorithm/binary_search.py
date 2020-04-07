def binary_search(numbers, number_to_find, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    number_to_find = int(input('Type a number: '))
    result = binary_search( numbers, number_to_find, 0, len(numbers)-1 )
    
    if result is True:
        print('the number {}, it was found on the list'.format(number_to_find))
    else:
        print('the number {} it wasn\'t found on the list'.format(number_to_find))