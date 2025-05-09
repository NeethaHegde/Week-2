def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        print(n,"is a not prime", )
    else:
        print(n,"is a prime",)
        
is_prime(6)
is_prime(5)