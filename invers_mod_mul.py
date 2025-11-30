def check_inverses_from_choices(a, m, choices):
    """
    Tester kun 'choices' for at se hvilke der er multiplikativ invers
    til tallet a modulo m. Udskriver ALLE resultater.
    """
    print(f"Tester hvilke af {choices} der er invers til {a} modulo {m}:\n")

    for c in choices:
        value = (a * c) % m
        if value == 1:
            print(f"{c}: ✔  {a} * {c} % {m} = 1  (INVERSE)")
        else:
            print(f"{c}: ❌  {a} * {c} % {m} = {value}")



a = 9
m = 10


choices = [1, 2, 9,10,17,19,23]

check_inverses_from_choices(a, m, choices)
