def ispalindrome():
    x=input("enter a word or phrase:")
    z=x[::-1]
    if x==z:
        print("It is palindrome:)")
    else:
        print("It is not a palindrome:(")

ispalindrome()
