#Prime number:
from math import sqrt
N = int(input())
prime_flag = 0
if(N > 1):
    for i in range(2, int(sqrt(N))+1):
        if(N % i == 0):
            prime_flag = 1
            break
    if(prime_flag == 0):
        print("True")
    else:
        print("False")
else:
    print("False")
    
