def InputInt(input):
    return input+10


print(InputInt(10))

li=list(map(InputInt,range(1,11)))

for x in li:
    print(x)



li= list(map(lambda x:x +10,range(1,11)))

for i in li:
    print(i)

print('=' * 50 )
li=(lambda  x,y:x+y)(1,2)
print(li)


print('=' * 50 )
li=(lambda  x,y,c:x+y+c)(1,2,3)
print(li)

#map(function,element...)
print('=' *  50)
li = list(map(lambda x:x,range(1,11)))
lilen=li.__len__()
print(lilen)

# print(li.__iter__().__next__())`
# print(li.__iter__().__next__())
array=li.__iter__()
init=1
while  init<=lilen:

    # array = li.__iter__() 새로운 방을 만든다

    print(array.__next__())



