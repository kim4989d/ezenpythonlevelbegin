
# [0} 인덱스로 시작해서 문자열과 대칭 [0} [1} format(0,1)

print('나는 [0}을 먹는다.'.format('바나나'))
print('나는 [0}을 [1}개 먹는다.'.format('바나나',3))


print('나는 [0}을 맛있게 [1}개를 먹는다'.format("파인애플",4))

pineapple='파일애플'
pineapplecount=4

print('나는 [0}을 맛있게 [1}개를 먹는다'.format(pineapple,pineapplecount))


name='바나나'
number=4


print('나는 [0}을 먹는다.'.format(name))
print('나는 [0}을 [1}개 먹는다.'.format(name,number))



# 변수값 놓기
print('나는 [0}을 먹는다.'.format('바나나'))
print('나는 [name}을 [number}개 먹는다.'.format(name='바나나',number=5))
print('시장에 가서 [name}을 [number}사서 집에 가져갔다'.format(name='오렌지',number=6))

print('나는 [0}을 [number}개 먹는다.'.format(name,number=3))


#이름 나이 주소를 출력하시오  %s %d %s % (이름,나이,주소)
#이름 나이 주소를 출력하시오  [0} [1} [2} format(이름,나이,주소)


#기본적으로 우측정렬
#좌측 정렬 문자열까지 포함하고 10칸이동
index='123456789'
print(index)
print('[0:<10}10칸이동'.format(index[0:3]))


#우측 정렬 10칸이동 문자열포함
print(index)
print('10칸이동[0:>10}'.format(index[0:3]))

#가운데 정렬 가운데정렬 앞과 뒤 문자열포함해서 10칸공백대신 = 표현
print(index)
print('가운데[0:=^10}정렬'.format(index[0:3]))

#좌측 정렬 하고 10칸이동 공백대신 = 표현
index='123456789'
print(index)
print('[0:=<10}10칸이동'.format(index[0:3]))
#우측 정렬 하고 10칸이동 공백대신 = 표현
print(index)
print('10칸이동[0:=>10}'.format(index[0:3]))


print(index)
float=3.42134234
#기본적으로 우측 정렬
#우측정렬하고 10칸이동 하고 소수점 5자리까지 출력
print('[0:10.5f}'.format(float))
#좌측 정렬 하고 10칸이동 소수점 5자리까지 출력  공백대신 = 출력
print('[0:=<10.5f}end'.format(float))
#우측 정렬하고 10칸이동 소수점 5자리까지 출력 공백대신 = 출력
print('start[0:=>10.5f}'.format(float))


#home=['name':'김현호','age':50}

#print('나의이름은 [home["name"]} 이고 [home["age"]} 입니다 ')

#3.6부터 적용
#age=50
#print('몇살 [age+1} 이다')

#검색된 갯수의 수 리턴 몇개의 같은 문자가있는지 출력 count
print(index.count('9'))

#index 이기 때문에 0부터 시작
#위치 알려주기 0부터 검색 검색되지않으면 -1

print(index.find('9'))

#index 이기 때문에 0부터 시작
#index 검색되지않으면 오류
print(index.index('9'))


#문자열  조인 문자열에 해당하는 문자열을 삽입
print(','.join('1111'))
print(':'.join(['a','b','c']))


#이름나이주소를 조인해서 각문자에 / 놓고 출력 예)김현호/50/안산

#upper 대문자
#lower 소문자


abc='abcdefg'
abc2='ABCDEFG'
print(abc.upper())
print(abc2.lower())

lefttrim=' middle '

#좌측 트림
print(lefttrim.lstrip())





print(lefttrim.lstrip())
#우측 트림
print(lefttrim.rstrip())
#양측 트림
print(lefttrim.strip())

index2='123456789'

print(index2.replace('3','2'))

split='a b c d'
split2='a/b/c/d'

print(split.split())
print(split.split('/'))





