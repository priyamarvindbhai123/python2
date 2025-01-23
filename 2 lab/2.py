#print largest and smallest value of 3

def is3():
    a=float(input("Enter the value of a:"))
    b=float(input("Enter the value of b:"))
    c=float(input("Enter the value of c:"))

    if b<a>c:
        print(a,"is largest number")

    elif c<b>a:
        print(b,"is largest number")

    elif b<c>a:
        print(c,"is largest number")

    else:
        print("all number are equal")

is3()
            
