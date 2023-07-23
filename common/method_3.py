def VarMethod1(*args,**args2):
    print(args)
    print(args2)

def VarMethod2(args,*args2):
    print(args)
    # print(args2)
    for i in args2:
        print(i)


def VarMethod3(args,*args2):
    print(args)
    # print(args2)
    for i in args2:
        print(i)


VarMethod1('김현호','아무개','이순신',김현호='김현호',아무개='아무개')
VarMethod2(1,[1,2,3])
VarMethod2(1,(1,2,3))
VarMethod3(1,{1:1,2:2,3:3})

