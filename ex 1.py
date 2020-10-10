inputNumber = int(input("Enter number to find next prime:   "))

def nextPrime(inputNum):

    for nextNumToChk in range(inputNum+1, inputNum +200):
        if nextNumToChk > 1:
# If num is divisible by any number between 2 and val, it is not prime

    for i in range(2, nextNumToChk):
        if (nextNumToChk % i) == 0:
            break
    else:
# Found the prime
    return nextNumToChk
result = nextPrime(inputNumber)
print "Next Prime is:   ", result
