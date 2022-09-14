print("Input lengths of the triangle sides:")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("equilateral")
elif x == y or x == z or y == z:
    print("isosceles")
else:
    print("Scalene triangle")
