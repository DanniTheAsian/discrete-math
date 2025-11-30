from math import gcd

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def solve_two(a1, m1, a2, m2):
    """
    Løs systemet:
        x ≡ a1 (mod m1)
        x ≡ a2 (mod m2)
    Returnerer (a, m) hvis der findes en løsning,
    hvor løsningen er x ≡ a (mod m).
    Returnerer None hvis der ingen løsning er.
    """
    g = gcd(m1, m2)

    if (a2 - a1) % g != 0:
        return None  

    m1_ = m1 // g
    m2_ = m2 // g

    _, s, _ = extended_gcd(m1_, m2_)
    k = ((a2 - a1) // g * s) % m2_


    x = (a1 + m1 * k) % (m1 * m2_ * g)
    M = m1 * m2_ * g
    return x, M

def solve_system(congruences):
    """
    congruences = [(a1, m1), (a2, m2), ...]
    """
    a, m = congruences[0]

    for ai, mi in congruences[1:]:
        result = solve_two(a, m, ai, mi)
        if result is None:
            return None
        a, m = result

    return a, m

def solution_between(congruences, limit=25000):
    solution = solve_system(congruences)
    if solution is None:
        return None

    a, m = solution
    a %= m
    if a <= limit:
        return a
    return None



system1 = [(2, 4), (3, 7), (10, 25), (7, 33)]
system2 = [(1, 2), (1, 3), (1, 4), (1, 5)]
system3 = [(1, 20), (2, 44)]

print("System 1:", solution_between(system1))
print("System 2:", solution_between(system2))
print("System 3:", solution_between(system3))
