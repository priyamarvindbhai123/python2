def binary(n):
    if n:
        print(n,n%2)
        return n%2 + (10 * binary(n//2))
    else:
        return n

print(binary(30))
