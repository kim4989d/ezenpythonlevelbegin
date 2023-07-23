def PrintEnd(a):
    #print(a,end ="")
    return a

def PrintEnd(b):
    print('sdddd')

a=PrintEnd('a')

print(a)


def Boolean(a,b):
    bool=True
    if a==1 and b==2:
        bool=True
    return bool


print(Boolean(1,2))
d
print('=' * 50 )

# 날짜 구하기
def KoreanNumber(input):
    week=['월','화','수','목','금','토','일']
    init=0
    choice=''
    for i in week:
        init = init + 1
        if init==input:
             choice=i
    return choice


print(KoreanNumber(7))










