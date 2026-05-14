def equilateral(sides):
    a, b, c = sides
    if a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b:
        if a == b == c:
            return True
    return False


def isosceles(sides):
    a, b, c = sides
    if a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b:
        if a == b or a == c or b == c:
            return True
        return False
    return False  


def scalene(sides):
    a, b, c = sides
    if a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b:
        if a != b and b != c and a != c:
            return True
        return False
    return False
