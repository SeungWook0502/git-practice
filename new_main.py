# Test python env

def print_hello():
    animals = ['dog','cat','hamster', 'tiger']
    foods = [
        'Spagetti',
        'Pizza',
        'bibimbob'
    ]
    names = [
        'Jeon',
        'hong',
        'Jane',
        'Oh',
        'Yong',
    ] # trailing comma
    for f_name in names:
        print(f'hello, {f_name}')

if __name__ == '__main__':
    print_hello()
