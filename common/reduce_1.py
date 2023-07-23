from functools import  reduce


re= reduce(lambda x,y:(x+y),range(1,11))

print(re)

# x + y 가 y + a 바뀌면 역으로 출력하면서 역으로 출력하면서 문자도 역으로 출력된다
re=reduce(lambda x,y:y+x,'abcdef')
print(re)

