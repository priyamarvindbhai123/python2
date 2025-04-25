#count number of digit and alphabet

def count():
    x=input("Enter a String:")

    d=0
    a=0

    for ch in x:

        if ch.isdigit()==True:
            d+=1

        elif ch.isalpha()==True:
            a+=1

        else:
            print("__")

    print("Digit in a string is:",d)
    print("Alphabet in string is:",a)

count()
