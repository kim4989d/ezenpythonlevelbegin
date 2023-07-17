doublequtterstr="kim hyunho"

singlequtterstr='kim hyunho'

case1str="kim's hyunho"
case2str="kim\'s hyunho"

#case1str='kim's hyunho' 안됨

case3str="\" ok \" sk"



print(doublequtterstr)
print(singlequtterstr)
print(case1str)
print(case2str)
print(case3str)



indexstr='123456789'

print(indexstr)
print(len(indexstr))

print(indexstr[0])
print(indexstr[5])
print(indexstr[8])

print(indexstr[-0])
print(indexstr[-5])
print(indexstr[-8])

print(indexstr[0:3])
print(indexstr[1:3])
print(indexstr[3:])
print(indexstr[6:-1])
print(indexstr[:5])
print(indexstr[4:6])


print("=====================================================")
#이름 나이 주소 출력
address='김현호 50 안산'
print('이름:',address[0:3])
print('나이:',address[4:6])
print('주소:',address[7:9])

print(address.split())



print("=====================================================")



#문제 python 을 pithon 으로 바뀌어서 출력하시오


python='python'
pithon=python[0]+'i'+python[2:]
print(pithon)

print("123\n")
print("456")
print("\\")
print("\'")
print("\"")
print("123\r")
print("123\f")
print("123\b")
print("123\000")
print("123456789")
print("123\t\t9")

#end 줄바꿈 없이 출력할수있도록
print("줄바꿈없이",end=" ")
print("출력 ")
print("출력2 ")


