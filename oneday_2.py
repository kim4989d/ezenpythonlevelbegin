hello='하이' * 5

print(hello)

#문자열길이

strlen='123456789'
print(len(strlen))

a='안녕'
b=' 하세요 '
print(a+b)

#문자열 str()

age=50
address='김현호 '+ str(age)+' 안산 '
print(address)

name='김현호'
who='나는 %s 입니다' %name
print(who)
who='나는 %name 입니다'
print(who)

age=50
who='나이는 %d' %age
print(who)

year =2023
month=7
day=14

print('현재날짜 %d-%02d-%02d'%(year,month,day))
height=173.5
print(height)
print('키는 %3f 입니다 ' %height)




