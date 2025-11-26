def C(n, r):
    """Returns how many combinations of n choose r."""
    return (factorial(n)//
            (factorial(r)*factorial(n-r))
            )

def P(n, r):
    """Returns how many permutations with n and r as input."""
    return (factorial(n)//
            factorial(n-r)
            )

# Auxilary Functions

def factorial(n: int) -> int:
    """Returns the factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
