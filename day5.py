
def addition(*args, verbose=False):
    """
    Adds any number of numeric values together.
    
    Parameters:
    - *args: numbers to be added
    - verbose (bool): if True, prints the operation

    Returns:
    - Sum of all numeric arguments
    """
    if not args:
        raise ValueError("At least one number must be provided.")

    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("All inputs must be int or float.")

    result = sum(args)

    if verbose:
        operation = " + ".join(str(x) for x in args)
        print(f"{operation} = {result}")

    return result

def addition(a, b):
 a + b

