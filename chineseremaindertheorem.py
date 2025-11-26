class ChineseRemainderTheorem:
    """
    Solver for Chinese Remainder Theorem systems.
    Prints all intermediate steps using the extended Euclidean algorithm.
    """

    def __init__(self, moduli: list[int], remainders: list[int]):
        if len(moduli) != len(remainders):
            raise ValueError("Moduli and remainders must have the same length")
        self.moduli = moduli
        self.remainders = remainders

    # --------------------------
    # Extended Euclidean Algorithm
    # --------------------------
    def _extended_gcd(self, a: int, b: int):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = self._extended_gcd(b, a % b)
        return g, y1, x1 - (a // b) * y1

    # --------------------------
    # Modular inverse
    # --------------------------
    def _mod_inverse(self, a: int, m: int) -> int:
        print(f"  Beregner invers af {a} modulo {m}:")
        g, x, y = self._extended_gcd(a, m)
        print(f"    gcd({a}, {m}) = {g}")

        if g != 1:
            raise ValueError(f"No modular inverse for {a} mod {m}")

        inv = x % m
        print(f"    Invers: {inv} (fordi {a}·{inv} ≡ 1 (mod {m}))")
        return inv

    # --------------------------
    # Solve CRT with explanation
    # --------------------------
    def solve(self) -> int:
        print("=== Chinese Remainder Theorem – Beregning ===")
        print(f"Moduli (m):     {self.moduli}")
        print(f"Remainders (a): {self.remainders}\n")

        # Step 1: total modulus
        M = 1
        for m in self.moduli:
            M *= m
        print(f"1) Samlet produkt M = {M}\n")

        Mi_list = []
        yi_list = []
        terms = []

        # Step 2: compute Mi, yi, term
        for i, (ai, mi) in enumerate(zip(self.remainders, self.moduli), start=1):
            print(f"== Trin {i}: Løs x ≡ {ai} (mod {mi}) ==")

            Mi = M // mi
            Mi_list.append(Mi)
            print(f"  M{i} = {M} / {mi} = {Mi}")

            # Modular inverse
            yi = self._mod_inverse(Mi, mi)
            yi_list.append(yi)

            term = ai * Mi * yi
            terms.append(term)
            print(f"  Term a{i}·M{i}·y{i} = {ai} · {Mi} · {yi} = {term}\n")

        # Step 3: CRT formula
        print("2) CRT-formlen:")
        symbolic = " + ".join([f"(a{i+1}·M{i+1}·y{i+1})" for i in range(len(terms))])
        concrete = " + ".join([f"({self.remainders[i]}·{Mi_list[i]}·{yi_list[i]})"
                               for i in range(len(terms))])
        print("   x = " + symbolic)
        print("   x = " + concrete)

        total_sum = sum(terms)
        print(f"\n   Numerisk sum = {total_sum}")

        # Step 4: reduce
        x = total_sum % M
        print(f"   x = {total_sum} mod {M} = {x}")
        print("=== Færdig ===\n")

        return x


# ---- Example usage ----
if __name__ == "__main__":
    moduli = [2, 3, 5, 11]
    remainders = [1, 2, 3, 4]

    crt = ChineseRemainderTheorem(moduli, remainders)
    solution = crt.solve()
    print("Solution:", solution)
