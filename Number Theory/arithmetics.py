def gcd(m: int, n: int) -> int:
    """Returns greatest common divisor of m and n
    using Euclides' algorithm.
    """
    if n == 0:
        return m
    else:
        return gcd(n,m % n)

def lcm(m: int, n: int) -> int:
    """Returns the least common multiple of m and n."""
    return int(m*(n/gcd(m,n)))


def modular_inverse(x: int, m: int) -> int:
    """Returns modular multiplicative inverse for x
    using naive approach.
    """
    a = 0
    for a in range(1,m):
        if ((x % m)*(a % m)) % m != 1:
            a += 1
        else:
            return a
    print(f"No modular inverse for {x}")


def is_relative_prime(a, b) -> bool:
    """Checks if a and b are realtive primes."""
    return gcd(a,b) == 1

def are_pairwise_prime(numbers: list[int]) -> bool:
    """Checks if the integers in a list are
    pairwise prime.
    """
    if len(numbers) == 2:
        return gcd(numbers[0],numbers[1]) == 1
    else:
        for number in numbers:
            new_numbers = numbers[:]
            new_numbers.remove(number)
            if not are_pairwise_prime(new_numbers):
                return False
    return True

def is_prime(n: int) -> bool:
    """Checks if n is a prime number."""
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for k in range(3,int(n**0.5)+1, 2):
        if n % k == 0:
            return False
    return True
