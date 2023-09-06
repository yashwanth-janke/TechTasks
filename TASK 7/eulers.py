#1- 3&5
def sum_of_multiples(a, b, n):
    total_sum = 0
    for i in range(n):
        if i % a == 0 or i % b == 0:
            total_sum += i
    return total_sum

for _ in range(int(input())):
    n = int(input())
    a = 3
    b = 5
    result = sum_of_multiples(a, b, n)
    print(result)

#2 Fibonacci terms
def sum(limit):
    a, b = 1, 2
    even_sum = 0

    while b <= limit:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b

    return even_sum

t = int(input())

for _ in range(t):
    n = int(input())
    result = sum(n)
    print(result)



#3 largest prime factor

def largest_prime_factor(n):
    largest_factor = 1
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i
    if n > 2:
        largest_factor = n
    return largest_factor

for _ in range(int(input())):
    n = int(input())
    result = largest_prime_factor(n)
    print(result)

#4 palindrome

def palin(num):
    return str(num) == str(num)[::-1]

def largepalin(limit):
    max = -1
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product < limit and palin(product):
                max = max(max, product)
    return max

for _ in range(int(input())):
    n = int(input())
    result = largepalin(n)
    print(result)


#5 (GCD)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result



for _ in range(int(input())):
    n = int(input())
    result = lcm(n)
    print(result)