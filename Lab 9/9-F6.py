def power123():
    lst=[]
    x=int(input("Enter a number:"))
    for i in range(1,x+1):
        tpl=(i,i**2,i**3)
        y=tuple(tpl)
        lst.append(y)

    print(lst)
    return lst

power123()
