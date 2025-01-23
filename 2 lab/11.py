#straight line

def sl():
    x1=float(input("Enter the value of x1:"))
    y1=float(input("Enter the value of y1:"))
    x2=float(input("Enter the value of x2:"))
    y2=float(input("Enter the value of y2:"))
    x3=float(input("Enter the value of x3:"))
    y3=float(input("Enter the value of y3:"))

    m1=(y2-y1)/(x2-x1)
    m2=(y3-y2)/(x3-x2)
    m=(y3-y1)/(x3-x1)

    if m1==m2==m:
        print("these 3 points are lies on a same straight line.")

    else:
        print("these 3 points are not lies on a same straight line.")
sl()
