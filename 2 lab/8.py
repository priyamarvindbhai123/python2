#validity of triangle

def vt():
    a=float(input("Enter the value of a angle in degree:"))
    b=float(input("Enter the value of b angle in degree:"))
    c=float(input("Enter the value of c angle in degree:"))

    if a+b+c==180:
        print("this is valid triangle.")

    else:
        print("this is not a valid triangle.")

vt()

    
