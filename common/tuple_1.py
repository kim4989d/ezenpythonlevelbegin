#list 는 [] 둘러싼다
#튜플(tuple)은 ()로 둘러싼다
#리스트는 요소갑 삽입 삭제 수정 이가능
# 튜플(tuple)은 요소값 변경 불가능


a=(1,2,3)
print(a)

# a[0]=2 요소값(element)변경 불가능
#print(a) 에러 변경불가능

print(a[0])
print(a[1])
print(a[2])

print(a[0:])


home=('김현호',50,('안산','상록수'))

print('이름은:' + home[0],end=" ")
print('나이는:' + str(home[1]))
print('주소는:'+ str(home[2][0:2]))

#str type
print(type(str(home[2][0:2])))
#tuple 타입
print(type(home[2][0:2]))

a=(1,2,3)
b=(4,5)

result =a+ b
print(result )
print('길이는:'+str(len(result)))








