money=3000

if(money==3000):
    print("참")
else:
    print("거짓")

a=1
b=2

print('=' * 30)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)
print(a<b)
print(a>b)

if money>2000 and money<5000:
    print('true')
else:
    print('false')

if money>2000 or  money<5000:
    print('true')
else:
    print('false')

#1이 포함되있으면
print(1 in [1,2,3])
#1이 포함되어있지 않으면
print(1 not in [1,2,3])


money=[1000,2000,3000]

if 3000 in money:
    print('택시를 타라')
else:
    print('걸어가라 ')



if 2000 in money:

    print('버스를 타라')
elif 1000 in money :
    print('걸어가라 ')

else:
    print('기어가라 ')

location=['서울','안산','시흥']

if '안산' in location:
    print(location[1]+'에 살아요 ')
else:
    print('사는 지역이없습니다 ')


#pass 해당하는문을 실행하지않음
if '오산' in location:pass

else:print('사는 지역이없습니다 ')
