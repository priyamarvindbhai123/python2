#area and para comp of rectangle

def apr():
    l=float(input("Enter the value of langth:"))
    b=float(input("Enter the value of breath:"))

    area=l*b
    para=2*(l+b)

    if area>para:
        print(area,">",para,"so area is greater")

    elif area<para:
        print(area,"<",para,"so perimater is greater")

    else:
        print("both are equal")

apr()
    
