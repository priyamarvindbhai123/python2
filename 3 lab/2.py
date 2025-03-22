'''
def cc():
    a=input("Enter a string:")

    print(a.lower())
    print(a.upper())
    print(a.title())
    print(a.capitalize())
    print(a.swapcase())

cc()
'''

def lower():
    str=input("Enter a string:")
    str1=""
    for ch in str:
        if ch>='A' and ch<+'z':
            str1=str1 + chr(ord(ch)+32)
        else:
            str1=str1+ch
    return str1

print(lower())
