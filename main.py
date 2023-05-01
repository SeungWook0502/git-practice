# Test python env

def print_hello():
    animals = ['dog','cat','hamster']
    foods = [
        'Spagetti',
        'Pizza'
    ]
    names = [
        'Jeon',
        'hong',
        'Jane',
    ] # trailing comma
    for f_name in names:
        print(f'hello, {f_name}')

if __name__ == '__main__':
    print_hello()
