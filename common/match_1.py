def printend(input):
    print(input, end=" ")


for i in range(1, 100):

    match(i%2,i%3):
        case (0, 0):
            printend(i)

        # case (0,_):
        #     print('0,_ true ')
        # case(_,0):
        #     print('_ 0 true ')

print('=' * 50)
for i in range(1, 10):

    if i == 8:
        break

    print(i)
