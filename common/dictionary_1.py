#dictionary->key value
#어떤 타입이든올수있다



home={'name':'김현호','age':50,'address':'안산'}

home2={'name':'김현호','age':50,'address':['안산','상록수']}


print(home['name'])
print(home['age'])
print(home['address'])


print(home2['address'][0:])

print(home)

print(home.keys())
print(home.values())


print(list(home.keys()))
print(list(home.values()))

a={1:1,2:2,3:3}

print(a[1])
print(a.get(1))


#print(a[4]) element 가없어서 에러 발생
print(a.get(4)) #에러업이 none로 표시

#none키를 찾으면 nonebase 출력
a.setdefault('none','nonebase')
print(a.get('none'))
#키가 nokey이면 키가없습니다 출력
a.get('nokey','키가없습니다')
#키가 5검색하면  키가없습니다 출력
print(a.get(5,'키가없습니다 '))
print(1 in a)
print(4 in a)





