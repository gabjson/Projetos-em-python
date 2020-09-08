def primo6(n) :
    if n % 2 == 0 : return n == 2
    divisor = 3
    raiz = int(n ** 0.5)
    while divisor <= raiz and n % divisor != 0 :
        divisor += 2
    return n > 1 and divisor > raiz

n = int(input())
while n != -1 :
    if primo6(n): print(1)
    else: print(0)
    n = int(input())
    
