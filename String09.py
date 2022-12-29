def main(x1,x2,x3):
    """
    Given three integers, x1, x2, and x3, return the "[x1, x2, x3]" string.
    Args:
        x1: int
        x2: int
        x3: int
    Returns:
        str: return answer.
    """
    a = "["+str(x1)+","+str(x2)+","+str(x3)+"]"
    return a
x1=2
x2=89
x3=7
print(main(x1,x2,x3))