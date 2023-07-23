init=0


result=0
while init<=10:
    result = result + init
    init = init + 1

    print(result)



print('=' * 50)
init=0

# while정상적으로 끝났을때  else 실행
# break 으로 빠져나오면 실행되지 않음


while init<=10:
    init=init+1
    if init==8:
        print(init)

else:
    print('발사 !!')

print('=' * 50 )

for i in range(1,10):
    print(i)


else:
    print(False)
