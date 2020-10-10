# Program to find the sum of all the divisors of a natural number


import math   
  
# Calculus of sum of all the divisors

def divSum(n) : 
    if(n == 1): 
       return 1
  
    # Result of sum
    result = 0
    
    # find all the divisors
    for i in range(2,(int)(math.sqrt(n))+1) : 
  
        # if 'i' is divisor of 'n' 
        if (n % i == 0) : 
  
            # if both divisors are the same, them add it only once; else, add both 
            if (i == (n/i)) : 
                result = result + i 
            else : 
                result = result + (i + n//i) 
          
    return (result + n + 1) 
    
# run program 
n = 30
print(divSum(n)) 
  