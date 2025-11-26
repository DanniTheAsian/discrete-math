PY_OPERATORS = ["and", "or", "==", "not", "!="]

TruthTable = tuple[str, list, list, list]


# ---------- Helper: extract subexpressions ----------

def extract_subexpressions(clean_expr: str) -> list[str]:
    subs: list[str] = []
    stack: list[int] = []

    for i, ch in enumerate(clean_expr):
        if ch == "(":
            stack.append(i)
        elif ch == ")" and stack:
            start = stack.pop()
            sub = clean_expr[start:i+1]
            if sub not in subs:
                subs.append(sub)

    if not subs:
        subs.append(clean_expr)

    if clean_expr not in subs:
        subs.append(clean_expr)

    return subs


# ---------- Operator translations ----------

def translate_ops(expression) -> str:
    translated_expression = []
    lst_expression = expression.split()
    i = 0
    while i < len(lst_expression):
        if lst_expression[i] == "imp":
            j = len(translated_expression) - 1
            bracket_balance = 0
            while j >= 0:
                if translated_expression[j] == ")":
                    bracket_balance -= 1
                elif translated_expression[j] == "(":
                    bracket_balance += 1
                if bracket_balance == 0:
                    translated_expression.insert(j, "not")
                    break
                j -= 1
            translated_expression.append("or")
        elif lst_expression[i] == "rimp":
            translated_expression.append("or")
            translated_expression.append("not")
        elif lst_expression[i] == "bimp":
            if lst_expression[i+1] == "not":
                translated_expression.append("!=")
                i += 1
            else:
                translated_expression.append("==")
        elif lst_expression[i] == "xor":
            if lst_expression[i+1] == "not":
                translated_expression.append("==")
                i += 1
            else:
                translated_expression.append("!=")
        else:
            translated_expression.append(lst_expression[i])
        i += 1
    return " ".join(translated_expression)


# ---------- Boolean evaluation ----------

def calc_bool(expression: str) -> bool:
    expression = expression.replace("not True", "False")
    expression = expression.replace("not False", "True")
    return eval(expression)


def bool_combinations(n: int) -> list[list[bool]]:
    results = []
    _bool_combinations(results, n, [])
    return results


def _bool_combinations(results: list, n: int, combination_list: list) -> None:
    if n == 0:
        results.append(combination_list)
    else:
        for value in [True, False]:
            if combination_list == []:
                _bool_combinations(results, n-1, [value])
            else:
                _bool_combinations(results, n-1, combination_list + [value])


def find_variables(expression: str) -> list[str]:
    unique_variables = []
    for sub in expression.split(" "):
        if sub not in unique_variables and sub not in (PY_OPERATORS + ["(", ")"]):
            unique_variables.append(sub)
    return unique_variables


def space_format(expression: str) -> str:
    spaced = ""
    for char in expression:
        if char == "(":
            spaced += char + " "
        elif char == "-":
            spaced += "not "
        elif char == ")":
            spaced += " " + char
        else:
            spaced += char
    return spaced


def remove_redundant_not(expression: str) -> str:
    stack = []
    for sub in expression.split():
        if stack and stack[-1] == "not" and sub == "not":
            stack.pop()
        else:
            stack.append(sub)
    return " ".join(stack)


# ---------- Standard truth table ----------

def generate_truthtable(expression: str) -> TruthTable:
    spaced = space_format(expression)
    translated = translate_ops(spaced)
    clean = remove_redundant_not(translated)

    variables = find_variables(clean)
    truth_rows = bool_combinations(len(variables))
    outputs = []

    for row in truth_rows:
        current = clean.split()
        for i, var in enumerate(variables):
            for j in range(len(current)):
                if current[j] == var:
                    current[j] = str(row[i])

        outputs.append(calc_bool(" ".join(current)))

    return (expression, variables, truth_rows, outputs)


# ---------- Pretty standard table ----------

def print_truthtable_pretty(expr: str) -> None:
    expression, variables, truth_rows, outputs = generate_truthtable(expr)

    print("\nTruth table for:", expression)
    print("-" * (6 * len(variables) + 12))

    header = "  ".join(f"{v:>5}" for v in variables) + "   |  OUT"
    print(header)
    print("-" * (len(header) + 2))

    for row, out in zip(truth_rows, outputs):
        row_str = "  ".join(str(val)[0].upper().rjust(5) for val in row)
        print(f"{row_str}   |   {str(out)[0].upper()}")

    print("-" * (len(header) + 2))


# ---------- Extended truth table ----------

def generate_extended_truthtable(expression: str) -> dict:
    spaced = space_format(expression)
    translated = translate_ops(spaced)
    clean = remove_redundant_not(translated)

    variables = find_variables(clean)
    truth_rows = bool_combinations(len(variables))
    subexprs = extract_subexpressions(clean)
    subresults = []

    for row in truth_rows:
        varmap = {var: row[i] for i, var in enumerate(variables)}
        rowvalues = []
        for sub in subexprs:
            tokens = sub.split()
            replaced = [str(varmap[t]) if t in varmap else t for t in tokens]
            rowvalues.append(calc_bool(" ".join(replaced)))
        subresults.append(rowvalues)

    return {
        "expression": expression,
        "variables": variables,
        "truth_rows": truth_rows,
        "subexpressions": subexprs,
        "subresults": subresults,
    }


def print_extended_truthtable(info: dict) -> None:
    vars = info["variables"]
    rows = info["truth_rows"]
    subs = info["subexpressions"]
    results = info["subresults"]

    print("\nExtended truth table for:", info["expression"])
    print("-" * 80)

    header = "  ".join(v.rjust(5) for v in vars)
    shead = " | ".join(subs)
    print(header + "   ||  " + shead)
    print("-" * 80)

    for row, vals in zip(rows, results):
        vpart = "  ".join(str(v)[0].upper().rjust(5) for v in row)
        spart = " | ".join(str(v)[0].upper() for v in vals)
        print(vpart + "   ||  " + spart)

    print("-" * 80)
