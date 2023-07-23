a=[1,2,3]
a2=[[1,2],[3,4],[5,6]]
b=(1,2,3)
c={1:1,2:2,3:3}

result=0
for i in a:
    print(i)




print('=' * 30)
for i in b:
    print(i)

print('=' * 30)
for i in c:
    print(i)

print('=' * 30)
for (first,last) in a2:
    print(first+last)


marks=[90,70,80,50,40]
number=0
for mark in marks:
    number=number+1

    if(mark>=60):
        print("%d 학생은 60점이상입니다 "% number)

    elif(mark>=50):
        print("%d 학생은 50점이상입니다 "% number)
    elif(mark>=40):
        print("%d 학생은 40점이상입니다 "% number)
    elif(mark>=30):
        print("%d 학생은 30점이상입니다 "% number)




