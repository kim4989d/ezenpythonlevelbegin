

a=[1,2,3,4]
b=[]

for i in a:
    b.append(i*3)

print(b)




two=0
a=[1,2,3,4,5,6,7,8,9]
b=[]
for i in a:
    if i%2==0:
     b.append(i)

print(b)

a=[1,2,3,4,5,6,7]
b=[ array for array in a if array%2==0 ]

print(b)

i=1

if i==1:
    print(i)
elif i==2:
    print(i)

a=[1,2,3,4]
print(a.pop(3))
print(a)

a=[1,2,3,4]
b=[]

from copy import copy
b=copy(a)
b=a
print(a is b)



