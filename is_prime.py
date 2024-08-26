from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def isPrime(n : int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1 , 2):
        if n % i == 0:
            return False
    return True

n = int(input())

if isPrime(n):
    print("YES")
else:
    print("NO")