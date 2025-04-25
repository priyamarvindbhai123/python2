import math

def is_prime(n):
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print("number is a prime number.")
else:
    print("number is not a prime number.")


def is_perfect(n):
    if n <= 1:
        return False
    
    divisors_sum = 0
    
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    
    return divisors_sum == n

number = int(input("Enter a number: "))
if is_perfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")


def is_armstrong(number):
    
    num_str = str(number)
    num_digits = len(num_str)
    
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    if sum_of_powers == number:
        return True
    else:
        return False


number = 153 
if is_armstrong(number):
    print(f"{number} is an Armstrong number!")
else:
    print(f"{number} is not an Armstrong number.")


def is_palindrome(number):
    num_str = str(number)
    
    if num_str == num_str[::-1]:
        return True
    else:
        return False

number = 111
if is_palindrome(number):
    print("number is a palindrome!")
else:
    print("number is not a palindrome.")


def is_automorphic(number):
    square = number ** 2
    
    number_str = str(number)
    square_str = str(square)
    
    if square_str.endswith(number_str):
        return True
    else:
        return False

number = 6 
if is_automorphic(number):
    print("number is an Automorphic number!")
else:
    print("number is not an Automorphic number.")
