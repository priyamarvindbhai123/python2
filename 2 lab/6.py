#num of digit

def nod():
    a=float(input("Enter a number:"))

    if 0<a<10 or -10<a<0:
        print(a,"is a 1 digit number.")

    elif 9<a<100 or (-100)<a<(-9):
        print(a,"is a 2 digit number.")

    elif 99<a<1000 or (-1000)<a<(-99):
        print(a,"is a 3 digit number.")

nod()
