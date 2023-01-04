def checkprime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def primeprint(n):
    for i in range(2,n+1):
        if checkprime(i) == True:
            print(i)
    pass

print(primeprint(1000))