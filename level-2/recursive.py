
while True:
    try:
        maximum = int(input('set a maximum for the sequence: '))
        break
    except ValueError:
        print('the input must be a number')


def fibonacci(first=1, second=1, max:int=maximum):

    print(first)
    
    if (second) > max: return 
    fibonacci(second, first+second)


fibonacci(max=maximum)
