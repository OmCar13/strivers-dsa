import math 

class Solution:
    def lcmAndGcd(self, A , B):
        arr = [0] * 2 
        
        gcd = math.gcd(A,B)
        lcm = (A*B) // gcd 
        
        arr[0], arr[1] = lcm, gcd 
        
        return arr