def power_set(a: set) -> list[any]:
    """Returns a list of all subsets of a set
    sorted by size of set.
    """
    result = []
    _power_set(result, a)
    result = [None] + sorted(result, key=len)
    return result

def _power_set(result: list, a: set) -> None:
    """A backtracking algorithm to find
    every possible subset of a set and add
    it to result.
    """
    for element in a:
        _power_set(result, a - {element})
    if len(a) > 0 and a not in result:
        result.append(a)
        
    
def cartesian_product(a: set, b: set) -> list[tuple[any]]:
    """Returns every pairing of one element
    from a and one element from b.
    """
    product = []
    for element_a in a:
        for element_b in b:
            product.append((element_a,element_b))
    return product
