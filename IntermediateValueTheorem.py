f = lambda x : x**2 #Fxn To graph

def findGivenC(n, intStart, intEnd):
    interval = 1
    while True:
        #print(n,intStart,intEnd)
        if f(intStart)==n:
            return intStart
        if f(intStart) < n < f(intEnd):
            intStart += interval
        else:
            intEnd = intStart
            intStart -=interval
            interval /= 10
        if interval < 10**-15:
            return (intStart,intEnd,interval)
        

print(findGivenC(63,0,100))