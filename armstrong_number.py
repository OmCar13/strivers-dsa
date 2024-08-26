def checkArmstrong(n):
    
    original_number = n
    count = 0

    if n == 0:
        return True
    if n < 0:
        return False
    
    while n != 0:
        n //= 10
        count += 1 
    
    n = original_number
    sum = 0 
    while n != 0:
        digit = n % 10 
        sum += digit ** count 
        n //= 10 

    return sum == original_number