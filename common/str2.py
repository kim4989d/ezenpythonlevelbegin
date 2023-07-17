
#문자열 곱하기

print("=" * 30)
print("문자열 곱하기 ")
print("=" * 30)


#문자열 길이
print('문자열길이:',len("123456789"))



#%s  문자열 %d 정수형 %f 실수형 %c 문자
#%s string :문자열 %d :decimal %f :float 실수형

print('나는 %s 맛있게 먹는다' % '파인애플')
eat=' %s 맛있게 먹는다' % '바나나'
print(eat)




print('나는 파인애플 %d개를 맛있게 먹는다' % 3)

eat=' %d개를 맛있게 먹는다' % 4
print(eat)


print('나는 %s %d개를 맛있게 먹는다' % ('파인애플',3))

eat=' %s %d개를 맛있게 먹는다' % ('바나나',4)
print(eat)



#이름 나이 주소 를 변수로 지정해서 출력하시오
#이름 name 나이 age 주소 address

print('=' * 30)

name='김현호'
age=50
home='안산'

print(' 이름은:%s 나이는:%d 주소는:%s' %(name,age,home))
print('=' * 30)


character ='a'
character2 ='b'
character3 ='c'
result=character + character2 + character3

print('문자:%c'% character)
print(result)

height=173.5

print('키는 %.2f 입니다 ' % height)
print('키는 %d 입니다 ' % height)


#생략가능 0은 모든실수형 표시 생략가능 %0.2f 소수점이하 2자리까지 표현
print('키는 %0.2f 입니다 ' % height)
print('키는 %.2f 입니다 ' % height)


#2%s 기본적으로 오른쪽 정렬 2칸 띄고 오른쪽 정렬해서 출력
index='123456789'



#오른쪽정렬에서 11칸 안에문자열포함하고 나머지는 공백
print(index)
print("오른쪽 정렬%11s"%index)



#오른쪽정렬하고 9칸문자열포함 나머지는 공백 문자열에서 0부터 2까지만 출력
print(index)
print('9칸 만들기%9s' %index[:3] )



#좌측 정렬 좌측으로 정렬 문자포함하고 나머진 공백 0부터 2까지 출력
print(index)
print('%-9s9칸만들기' %index[:3])

#0은 길이에 상관없이 생략가능하고 0.4 소수점포인트 위치 소수점뒤에나오는숫자갯수

#실수형 출력 소수점이하 4자리까지 출력
print('%0.4f' % 3.42134234)

print('123456789')
#기본적으로 우측정렬이고 10칸의공간을 만드는데 출력포함해서 출력 0은 모든 문자 출력
print('%10.4f' % 3.42134234)
















