
result=0

def add(num):
    # global 전역변수 쓰겠다
    global  result
    result =result+num
    print(result)

add(1)
add(2)
print(result)
