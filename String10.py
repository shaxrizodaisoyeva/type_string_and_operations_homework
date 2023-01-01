def main(x,y):
    """
    Given three integers, x, y, return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    b=(x+y)*2
    a = "("+str(x)+"+"+str(y)+")"+'*'+str(2)+'='+str({b})
    return a
x =7
y =6
print(main(x,y))