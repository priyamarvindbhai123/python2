#grade system

def gs():
    p=float(input("Enter the obtained marks in physics:"))
    c=float(input("Enter the obtained marks in chemistry:"))
    m=float(input("Enter the obtained marks in maths:"))

    total=p+c+m
    print("your total obtained marks is:",total)

    avg=total/3
    print("your average marks is:",avg)

    if 80<=p<=100:
        print("you got",p,"marks and grade 'O' in physics.")

    elif 70<=p<=79:
        print("you got",p,"marks and grade 'A+' in physics.")

    elif 60<=p<=69:
        print("you got",p,"marks and grade 'A' in physics.")

    elif 55<=p<=59:
        print("you got",p,"marks and grade 'B+' in physics.")

    elif 50<=p<=54:
        print("you got",p,"marks and grade 'B' in physics.")

    elif 45<=p<=49:
        print("you got",p,"marks and grade 'C' in physics.")

    elif 40<=p<=44:
        print("you got",p,"marks and grade 'P' in physics.")

    elif 0<=p<=39:
        print("you got",p,"marks and grade 'F' in physics and you are fail in this subject.")

    else:
        print("you are absent in physics.")

    if 80<=c<=100:
        print("you got",c,"marks and grade 'O' in chemistry.")

    elif 70<=c<=79:
        print("you got",c,"marks and grade 'A+' in chemistry.")

    elif 60<=c<=69:
        print("you got",c,"marks and grade 'A' in chemistry.")

    elif 55<=c<=59:
        print("you got",c,"marks and grade 'B+' in chemistry.")

    elif 50<=c<=54:
        print("you got",c,"marks and grade 'B' in chemistry.")

    elif 45<=c<=49:
        print("you got",c,"marks and grade 'C' in chemistry.")

    elif 40<=c<=44:
        print("you got",c,"marks and grade 'P' in chemistry.")

    elif 0<=c<=39:
        print("you got",c,"marks and grade 'F' in chemistry and you are fail in this subject.")

    else:
        print("you are absent in chemisty.")

    if 80<=m<=100:
        print("you got",m,"marks and grade 'O' in maths.")

    elif 70<=m<=79:
        print("you got",m,"marks and grade 'A+' in maths.")

    elif 60<=m<=69:
        print("you got",m,"marks and grade 'A' in maths.")

    elif 55<=m<=59:
        print("you got",m,"marks and grade 'B+' in maths.")

    elif 50<=m<=54:
        print("you got",m,"marks and grade 'B' in maths.")

    elif 45<=m<=49:
        print("you got",m,"marks and grade 'C' in maths.")

    elif 40<=m<=44:
        print("you got",m,"marks and grade 'P' in maths.")

    elif 0<=m<=39:
        print("you got",m,"marks and grade 'F' in maths and you are fail in this subject.")

    else:
        print("you are absent in maths.")

gs()
        


        


        
