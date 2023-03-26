import math
n = int(input("Numar "))
x = n
def isPrime(n):
    ok = True
    for d in range(2,int(math.sqrt(n))+1):
        if n % d == 0: 
            return False
    return True
            
while x:
    if n < 2:
        print("Nu e prim")
        break
    if isPrime(x):
        print(x)
        break
    x = x - 1
