a=set([1,2,3])

print(a)

#index 가없으므로 값에 접근하지못한다
#print(a[0])

#set 중복허용않함  순서가 없다
#list tuple 는 ordered 이지만 set unordered 이다


str=set("hello")
str2=set("35147")


print(str)
print(str2)

print('=' * 30 )
a=list(a)
print(a[0])

str=list(str)

print(str)
print(str.sort()) #none

str2=list(str2)
print(str2.sort())

print('=' * 30 )
a=set([1,2,3])

str=set("hello")
str2=set("35147")


a=tuple(a)
print(a[0])

str=tuple(str)

print(str)
#print(str.sort()) #tuple 지원하지않음

str2=tuple(str2)
#print(str2.sort()) #tuple 지원하지않음


a=set([1,2,3])
b=set([3,4,5])

#교집합
#
intersection=a & b
print(intersection)

#합집합
sum =a | b

print(sum)

sum= a.union(b)
print(sum)
#차집합
subtraction= a-b
print(subtraction)

#차집합
subtraction=a.difference(b)
print(subtraction)

a=set([1,2,3])

a.add(4)
print(a)

a=set([1,2,3])
a.update([4,5,6])
print(a)

a=set([1,2,3])
a.remove(2)
print(a)