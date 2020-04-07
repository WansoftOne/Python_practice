def run():
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))

def run2():
    counter = 0
    with open('aleph.txt') as f:
        print(f.readlines()) #Read al lines
        for line in f:
             counter += line.count('Beatriz')
    print('Beatriz is {} times on the text'.format(counter))

if __name__ == '__main__':
    run()