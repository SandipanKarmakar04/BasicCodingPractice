def circleArea(r):
    pi = 3.14

    if r < 1:
        return "radius cannot be negative."
    area = pi * r * r
    return area

r = float(input("Enter the radius of circle"))
res = circleArea(r)
print(res)
