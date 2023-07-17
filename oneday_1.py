print('안녕하세요 오신것을 환영합니다 .')
print('=========================')
print("쌍따움표라고도 하고 더블쿼터 라고도합니다 .")

name='김현호'
age=50
address='안산'

print(name,age,address)

print(type(name))
print(type(age))

#인덱스 0부터 시작
print('================================')


index='123456789'

print(index)
print(index[0])
print(index[8])
print(index[0:3])
print(index[0:5])
print(index[-1])
print(index[-3])
print(index[-9])

print(index[-4:-2])


print('==================')

a=True
b=False

print('참?',a)
print('거짓',b)
print(type(a))


a=6
b=2

print(a)
print(b)
print(type(a))

print(a+b)
print(a * b)
print(a/b)
print(a%b)


a=7
b=3

#거듭제곱

print(a/b)
print(a//b)
 #2x2x2x2x2x2
#2 4 8 16 32 64
a=2**6
print(a)

#10x10x10

b=10**3
print(b)

#할당연산자
x=10
x+=20

print(x)


x=3
y=5
x*=x+y #x=x*(x+y)
print(x)

