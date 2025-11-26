from truthtable import (
    generate_truthtable,
    print_truthtable_pretty,
    generate_extended_truthtable,
    print_extended_truthtable,
)

def auto_parenthesize(expr: str) -> str:
    if "(" in expr or ")" in expr:
        return expr

    tokens = expr.split()

    def fold_not(tokens):
        i = 0
        while i < len(tokens):
            if tokens[i] == "not" and i < len(tokens)-1:
                tokens[i:i+2] = [f"(not {tokens[i+1]})"]
            else:
                i += 1
        return tokens

    def fold_binary(tokens, op):
        i = 0
        while i < len(tokens):
            if tokens[i] == op and 0 < i < len(tokens)-1:
                left = tokens[i-1]
                right = tokens[i+1]
                tokens[i-1:i+2] = [f"({left} {op} {right})"]
                i -= 1
            else:
                i += 1
        return tokens

    tokens = fold_not(tokens)
    tokens = fold_binary(tokens, "and")
    tokens = fold_binary(tokens, "xor")
    tokens = fold_binary(tokens, "or")

    return " ".join(tokens)


def get_outputs(expr: str) -> list[bool]:
    expr = auto_parenthesize(expr)
    return generate_truthtable(expr)[3]


def is_tautology(expr: str) -> bool:
    return all(get_outputs(expr))


def is_contradiction(expr: str) -> bool:
    return not any(get_outputs(expr))


def is_contingency(expr: str) -> bool:
    out = get_outputs(expr)
    return any(out) and not all(out)


def is_equivalent(a: str, b: str) -> bool:
    a2 = auto_parenthesize(a)
    b2 = auto_parenthesize(b)
    comp = f"({a2}) bimp ({b2})"
    return all(get_outputs(comp))


def main():
    choice = input("1=ækvivalens, 2=klassificér udsagn, 3=udvidet tabel: ")

    if choice == "1":
        e1 = input("Udsagn 1: ")
        e2 = input("Udsagn 2: ")
        print("Equivalent:", is_equivalent(e1, e2))

    elif choice == "2":
        e = input("Udsagn: ")
        ep = auto_parenthesize(e)
        print("Tautology:", is_tautology(ep))
        print("Contradiction:", is_contradiction(ep))
        print("Contingency:", is_contingency(ep))


    elif choice == "3":
        e = input("Udsagn: ")
        ep = auto_parenthesize(e)
        info = generate_extended_truthtable(ep)
        print_extended_truthtable(info)

    else:
        print("Ugyldigt valg")


if __name__ == "__main__":
    main()
