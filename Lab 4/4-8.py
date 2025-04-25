#factorial

def fact():
    x=int(input("Enter a number:"))
    f=1

    for i in range(1,x+1):
        f=f*i
    print("factorial of",x,"is:",f,)

fact()
