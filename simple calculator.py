#program for simple calculator
def add(x,y):
    return (x+y)
def sub(x,y):
    return (x-y)
def mul(x,y):
    return (x*y)
def div(x,y):
    return (x/y)
def power(x,y):
    return(x**y)
def mainmenu():
    print("enter the operation to perform")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.division")
    print("5.power")
    choice=int(input("enter the choice:"))

    if choice ==1:
        n1=int(input("enter the first number:"))
        n2=int(input("enter the second number:"))
        print("sum of 2 numbers is:",add(n1,n2))
        mainmenu()
    elif choice ==2:
        n1=int(input("enter the first number:"))
        n2=int(input("enter the second number:"))
        print("Difference of 2 numbers is:",sub(n1,n2))
        mainmenu()
    elif choice ==3:
        n1=int(input("enter the first number:"))
        n2=int(input("enter the second number:"))
        print("product of 2 numbers is:",mul(n1,n2))
        mainmenu()
    elif choice ==4:
        n1=int(input("enter the first number:"))
        n2=int(input("enter the second number:"))
        print("division of 2 numbers is:",div(n1,n2))
        mainmenu()
    elif choice ==5:
        n1=int(input("enter the first number:"))
        n2=int(input("enter the second number:"))
        print("power is:",power(n1,n2))
        mainmenu()
    else:
        print("invalid option,please try again")
mainmenu()
