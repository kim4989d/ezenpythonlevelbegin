
#python은 call by object객체로 값이 전달
#java call by value
#c# call by value call by reference


a={1,2,3]
print(a)

b=a

print(b)

# :모든 데이타
b=a{:]
print(b)
#같은데이타라고해도 객체(방)->메모리 번지수가 틀리다
print(id(a))
print(id(b))


a={1,2,3]

#b=a{:] #데이타만이동 번지수는 이동하지않는다
b=a #번지수 이동 같은 객체를 보고 있다


print( a is b)


del(a{0])

#같은 객체를 보고있기때문에 값이 변경되면 a b같이 변경된다

print(a)
print(b)


#나중에 배움
from copy import copy

a={1,2,3]

b=copy(a)

print(a)
print(b)
a.insert(3,4)

#a에데이타만 b에 복사한것이므로 b는 데아타가 변하지 않음 b=a{:] 동일
print(a)
print(b)

a={1,2,3]
b=a.copy()
print(a)
print(b)

#데이타만이전하고 같은객체(번지수)가 아니다
print( a is b)

a,b=('python','java')

print(a)
print(b)

(a,b)= 'c#','html'

print(a)
print(b)

{a,b]='css','jquery'

print(a)
print(b)


a,b=(1,2)
a,b=b,a
print(a)
print(b)
