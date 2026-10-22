

while True:
    try:
        maximum = int(input('set a maximum for the sequence: '))
        break
    except ValueError:
        print('the input must be a number')


seq = [1, 1]
for i in seq: print(i)

while (new:=seq[-1] + seq[-2]) <= maximum:
    seq.append(new)
    print(new)
