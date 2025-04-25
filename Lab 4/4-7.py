#ncr and npr

def pnc():
    n=int(input("Enter a value of n:"))
    r=int(input("Enter a value of r:"))

    if n>r:
        
        fn=1
        for i in range(1,n+1):
            fn=fn*i

        fr=1
        for i in range(1,r+1):
            fr=fr*i

        fnr=1
        for i in range(1,(n-r)+1):
            fnr=fnr*i

        ncr=fn/(fr*fnr)

        print("ncr=",ncr)


        npr=fn/(fnr)

        print("npr=",npr)

    else:
        print("We cann't find PNC because",n,"<",r)

pnc()
    
