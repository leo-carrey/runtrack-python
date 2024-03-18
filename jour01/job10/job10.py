def check_if_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_number(n):
    for i in range(2, n+1):
        if check_if_prime(i) == True:
            print(i)

prime_number(1000)
