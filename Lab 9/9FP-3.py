import random
def square(l1):
    return l1**2
lst=[]
for i in range(10):
    lst.append(random.randint(-15,15))
print(list(map(square,lst)))
