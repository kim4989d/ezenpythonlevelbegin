
a=[1,2,3]


#index배열이기때문에 0부터 시작
print(a[0])
print(a[1])
print(a[2])

# -1은뒤에서 시작
print(a[-1])

#배열안에 배열
a=[1,2,[1,2,3]]

print(a[0])
print(a[1])
print(a[2])

#행 열 :행은 그행의 열을 나타나며
print(a[-1][0])
print(a[-1][1])
print(a[2][2])

a=[1,2,[1,2,[1,2]]]

#배열안에 배열안에 배열
#2번째 안에 2번째 안에 열로 접근 0번째
print(a[2][2][0])

#2번째 안에 2번째 안에 열로 접근 1번째
print(a[-1][2][1])



#슬라이싱으로 접근
home=['김현호',50,'안산']

print(home[0:3])
print(home[:2])
print(home[1:])


home=['김현호',50,['안산','상록구']]



print('이름은 {0}'.format(home[0]) )
print('주소는 {0} '.format(home[2][0:2]))

print('이름은 %s'% home[0],end=" ")
print('주소는 %s '%home[2][0:2])



#2번째안에 0번째 얼에 접근
print(home[2][0:])




a=[1,2,3]
#배열의 갯수을 나타내며 1부터 시작
print('길이:',len(a))

#a배열에 3곱하기 그대로 3배의 크기가 나옴
result=a*3
print(result)

#숫자 문자여서 오류 발생형변환(casting) 해주어야함
# print(a[0]+'hi')
print(type(str(a[0])+'hi'))

#list 값 수정
a[0]=5
print(a[0])


#해당하는 배열요소 삭제
del(a[0])
print(a)


a=[1,2,3]
#슬라이싱으로 삭제
del(a[1:])
print(a)



#append 배열요소 추가
a=[1,2,3]

a.append(4)
print(a)

a=[3,1,2]
a.sort()
print(a)

#sort 알파벳 정렬
a=['b','c','a']

a.sort()
print(a)

a=['a','b','c']

a.reverse()

print(a)

#index 해당하는 타입의 위치
a=[1,2,3]
b=['a','b','c']
print('위치는:',a.index(3))
print('위치는:',b.index('a'))


#insert 해당하는 list 요소 삽입

a=[1,2,3]
a.insert(0,4)
print(a)

#remove 해당하는요소제거
a=[1,2,3]
b=['a','b','c']

a.remove(1)
print(a)

b.remove('c')
print(b)


#pop 마지막 요소 제거

a=[1,2,3]
a.pop()
print(a)

a=[1,2,3]
print(a.pop(2))
print(a)

#list 요소 같은 문자 갯수 count
a=[1,2,3,1]
print(a.count(1))

a=[1,2,3]
a.extend([4,5])
print(a)

a=[1,2,3]
b=[4,5]

a.extend(b)
print(a)

