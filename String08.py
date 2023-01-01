def main(first,last):
    """
    Given two strings, first_name and last_name, return a single string in the format "last, first".
    Args:
        first: str
        last: str
    Returns:
        str: return answer.
    """
    x = str(last)+","+str(first)
    return x 
last = "Isoeva"
first = "Shakhrizoda"
print(main(first,last))