def Sum(x,y):
    return x+y




print(Sum(1,2))


# lambda 매개변수 : 표현식

print('=' * 50 )
sum=(lambda  x,y:x+y)(10,20)
print(sum)


print('='  * 50 )
map=map(lambda x,y:x *2,range(1,10))


li= list(map)

print(li)

