# Check if a number is prime.

n = 29
is_prime = True
if n > 1:
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f'{n} is prime.')
else:
    print(f'{n} is not prime.')
