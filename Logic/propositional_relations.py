from truthtable import *


# Syntax of expressions should be written as specified in main() of "truthtable.py"

def is_equivalent(expression_1, expression_2) -> bool:
    """Checks if two propositions has same truthvalues."""
    compound = f"({expression_1}) bimp ({expression_2})"
    return all(generate_truthtable(compound)[3])

def is_tautology(expression) -> bool:
    """Checks if a proposition always is True."""
    truthtable = generate_truthtable(expression)
    outputs = truthtable[3]
    return all(outputs)

def is_contingency(expression) -> bool:
    """Checks if a proposition sometimes is True
    and sometimes is False.
    """
    truthtable = generate_truthtable(expression)
    outputs = truthtable[3]
    return any(outputs) and not all(outputs)

def is_contradiction(expression) -> bool:
    """Checks if a proposition always is False"""
    truthtable = generate_truthtable(expression)
    outputs = truthtable[3]
    return not any(outputs)

if __name__ == "__main__":
   def main():

    print("\nEksempel på store kæder du nu kan skrive:")
    print("  p and q or p or q")
    print("  p and q or -r imp s xor t")
    print("  -p and q and r or s xor -t")
    print()

    choice = input("1 = ækvivalens, 2 = klassificér udsagn: ")

    if choice == "1":
        e1 = input("Udsagn 1: ")
        e2 = input("Udsagn 2: ")
        print(is_equivalent(e1, e2))
        print_truthtable_pretty(f"({e1}) bimp ({e2})")

    elif choice == "2":
        e = input("Udsagn: ")
        print("Tautology:", is_tautology(e))
        print("Contradiction:", is_contradiction(e))
        print("Contingency:", is_contingency(e))
        print_truthtable_pretty(e)

    else:
        print("Ugyldigt valg")
