def printend(input):
    print(input,end="\t")


for i in range(2,10):
    for x in range(1,10):
        printend('{0} x {1} = {2}'.format(i,x,i*x))
    print()


print('=' * 50 )


for x in range(1,10):
    for i in range(2,10):
        printend("{0} x {1}= {2}".format(i,x,i*x))
    print()





