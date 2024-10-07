def add():
    a=int(input("enter a 1st number"))
    b=int(input("enter a 2nd number"))
    print(a+b)
def sub():
    a=int(input("enter a 1st number"))
    b=int(input("enter a 2nd number"))
    print(a-b)
def mul():
    a=int(input("enter a 1st number"))
    b=int(input("enter a 2nd number"))
    print(a*b)
def div():
    a=int(input("enter a 1st number"))
    b=int(input("enter a 2nd number"))
    print(a/b)
def mod():
    a=int(input("enter a 1st number"))
    b=int(input("enter a 2nd number"))
    print(a%b)
while True:
    print('''
    1.add
    2.sub
    3.mul
    4.div
    5.mod
    6.exit'''
    )
    ch=int(input("enter the choice"))
    if ch==1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        mul()
    elif ch==4:
        div()
    elif ch==5:
        mod()
    elif ch==6:
        break
    else:
        print("invalid input")
        