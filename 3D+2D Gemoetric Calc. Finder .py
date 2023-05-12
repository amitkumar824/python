line = "\n<" + "-" * 30 + " RESTART " + "-" * 30 + ">"
line2 = "«" * 35 + "»" * 35


def l():
    l = float(input("Enter the value of Length:- "))
    return l


def b():
    b = float(input("Enter the value of Breadth:- "))
    return b


def h():
    h = float(input("Enter the value of Height:- "))
    return h


def r():
    r = float(input("Enter the value of Radius:- "))
    return r


def a():
    a = float(input("Enter the value of Side:- "))
    return a


def big_r():
    big_r = float(input("Enter the value of Bigger Radius:- "))
    return big_r


class Three_D:
    class Cube:

        def volume(a):
            print(f"The volume is = {a ** 3} cubic unit \n{line}")

        def csa(a):
            print(f"The C.S.A is = {4 * a ** 2} sq.unit \n{line}")

        def tsa(a):
            print(f"The T.S.A is = {6 * a ** 2} sq. unit \n{line}")

        def diagonal(a):
            print(f"The diagonal is = {a * 3 ** 0.5} unit \n{line}")

    class Cuboid:

        def volume(l, b, h):
            print(f"The volume is = {l * b * h} cubic unit \n{line}")

        def csa(l, b, h):
            print(f"The C.S.A is = {2 * (l + b) * h} sq. unit \n{line}")

        def tsa(l, b, h):
            print(f"The T.S.A is = {2 * (l * b + b * h + h * l)} sq. unit \n{line}")

        def diagonal(l, b, h):
            print(f"The diagonal is = {(l ** 2 + b ** 2 + h ** 2) ** 0.5} unit \n{line}")

    class Cylinder:

        def volume(r, h):
            print(f"The volume is = {(22 / 7) * r ** 2 * h} cubic unit \n{line}")

        def csa(r, h):
            print(f"The C.S.A is = {2 * (22 / 7) * r * h} sq. unit \n{line}")

        def tsa(r, h):
            print(f"The T.S.A is = {2 * (22 / 7) * r * (h + r)} sq. unit \n{line}")

    class Cone:

        def volume(r, h):
            print(f"The volume is = {(1 / 3) * (22 / 7) * r ** 2 * h} cubic unit \n{line}")

        def csa(r, l):
            print(f"The C.S.A is = {(22 / 7) * r * l} sq. unit \n{line}")

        def tsa(r, l):
            print(f"The T.S.A is = {(22 / 7) * r * (l + r)} sq. unit \n{line}")

        def slant_height(r, h):
            print(f"The Slant Height is = {(r * r + h * h) ** 0.5} unit \n{line}")

    class Sphere:

        def volume(r):
            print(f"The volume is = {(4 / 3) * (22 / 7) * r ** 3} cubic unit \n{line}")

        def csa(r):
            print(f"The C.S.A is = {4 * (22 / 7) * r ** 2} sq.unit \n{line}")

        def tsa(r):
            print(f"The T.S.A is = {4 * (22 / 7) * r ** 2} sq. unit \n{line}")

    class Hemi_Sphere:

        def volume(r):
            print(f"The volume is = {(2 / 3) * (22 / 7) * r ** 3} cubic unit \n{line}")

        def csa(r):
            print(f"The C.S.A is = {2 * (22 / 7) * r ** 3} sq.unit \n{line}")

        def tsa(r):
            print(f"The T.S.A is = {3 * (22 / 7) * r ** 3} sq. unit \n{line}")

    class Frustum:

        def volume(r, big_r, h):
            print(f"The volume is = ~{(1 / 3) * (22 / 7) * h * (big_r ** 2 + r ** 2 + big_r * r)} cubic unit \n{line}")

        def csa(r, big_r, l):
            print(f"The C.S.A is = {(22 / 7) * l * (big_r + r)} sq.unit \n{line}")

        def tsa(r, big_r, l):
            print(f"The T.S.A is = {(22 / 7) * (big_r ** 2 + r ** 2 + l * (big_r + r))} sq. unit \n{line}")

        def slant_height(r, big_r, h):
            print(f"The Slant Height is = {(h * h + (big_r - r) ** 2) ** 0.5} unit \n{line}")


class Two_D:
    class Square:

        def area(a):
            print(f"The Area is = {a ** 2} sq. unit \n{line}")

        def parimeter(a):
            print(f"The Parameter is = {a * 4} unit \n{line}")

    class Rectangle:

        def area(l, b):
            print(f"The Area is = {l * b} sq. unit \n{line}")

        def parimeter(l, b):
            print(f"The Parameter is = {2 * (l + b)} unit \n{line}")

    class Circle:

        def area(r):
            print(f"The area is = {(22 / 7) * r ** 2} sq. unit \n{line}")

        def circumference(r):
            print(f"The circumference is = {2 * (22 / 7) * r} unit \n{line}")

        def diameter(r):
            print(f"The diameter is = {2 * r} unit \n{line}")

    class Triangle:

        def area(b, h):
            print(f"The area is = {(1 / 2) * b * h} sq. unit \n{line}")

        def Parameter(s1, s2, s3):
            print(f"The Parameter is = {s1 + s2 + s3} unit \n{line}")


if __name__ == '__main__':

    try:
        while True:
            print(
                "1. Cube\t\t\t\t\t8. Square\n2. Cuboid\t\t\t\t9. Rectangle\n3. Cylinder\t\t\t\t10. Circle\n4. Cone\t\t\t\t\t11. Triangle"
                f"\n5. Sphere\n6. Hemi Sphere\n7. Frustum\n{line2}")
            n = input("\nEnter your choice:- ")

            if n == '1' or n == 'cube' or n == 'Cube':  # Cube
                q = int(
                    input("\nWhat do you want to find in Cube?... \n1. Volume\n2. C.S.A\n3. T.S.A\n4. Diagonal\n>>> "))
                if q == 1:
                    Three_D.Cube.volume(a())

                elif q == 2:
                    Three_D.Cube.csa(a())

                elif q == 3:
                    Three_D.Cube.tsa(a())

                elif q == 4:
                    Three_D.Cube.diagonal(a())

                else:
                    print("Something is wrong... Try Again!!")
                    continue

            elif n == '2' or n == 'cuboid' or n == 'Cuboid':  # cuboid
                q = int(
                    input(
                        "\nWhat do you want to find in Cuboid?... \n1. Volume\n2. C.S.A\n3. T.S.A\n4. Diagonal\n>>> "))

                if q == 1:
                    Three_D.Cuboid.volume(l(), b(), h())

                elif q == 2:
                    Three_D.Cuboid.csa(l(), b(), h())

                elif q == 3:
                    Three_D.Cuboid.tsa(l(), b(), h())

                elif q == 4:
                    Three_D.Cuboid.diagonal(l(), b(), h())

                else:
                    print("Something is wrong... Try Again!!")
                    continue

            elif n == '3' or n == 'sphere' or n == 'Sphere':  # cylinder
                q = int(input("\nWhat do you want to find in Cylinder?... \n1. Volume\n2. C.S.A\n3. T.S.A\n>>> "))
                if q == 1:
                    Three_D.Cylinder.volume(r(), h())

                elif q == 2:
                    Three_D.Cylinder.csa(r(), h())

                elif q == 3:
                    Three_D.Cylinder.tsa(r(), h())

                else:
                    print("Something is wrong... Try Again!!")
                    continue

            elif n == '4' or n == 'cone' or n == 'Cone':  # cone
                q = int(
                    input(
                        "\nWhat do you want to find in Cone?... \n1. Volume\n2. C.S.A\n3. T.S.A\n4. Slant Height\n>>> "))
                if q == 1:
                    Three_D.Cone.volume(r(), h())

                elif q == 2:
                    Three_D.Cone.csa(r(), l())

                elif q == 3:
                    Three_D.Cone.tsa(r(), l())

                elif q == 4:
                    Three_D.Cone.slant_height(r(), h())

                else:
                    print("Something is wrong... Try Again!!!")
                    continue

            elif n == '5' or n == 'sphere' or n == 'Sphere':  # sphere
                q = int(input("\nWhat do you want to find in Sphere?... \n1. Volume\n2. C.S.A\n3. T.S.A\n>>> "))
                if q == 1:
                    Three_D.Sphere.volume(r())

                elif q == 2:
                    Three_D.Sphere.csa(r())

                elif q == 3:
                    Three_D.Sphere.tsa(r())

                else:
                    print("Something is wrong... Try Again!!")
                    continue

            elif n == '6' or n == 'hemisphere' or n == 'Hemisphere' or n == 'hemi-sphere':  # hemi-sphere
                q = int(input("\nWhat do you want to find in Hemi-Sphere?... \n1. Volume\n2. C.S.A\n3. T.S.A\n>>> "))
                if q == 1:
                    Three_D.Hemi_Sphere.volume(r())

                elif q == 2:
                    Three_D.Hemi_Sphere.csa(r())

                elif q == 3:
                    Three_D.Hemi_Sphere.tsa(r())

                else:
                    print("Something is wrong... Try Again!!")
                    continue

            elif n == '7' or n == 'frustum' or n == 'Frustum':
                q = int(
                    input(
                        "\nWhat do you want to find in Frustum?... \n1. Volume\n2. C.S.A\n3. T.S.A\n4. Slant Height\n>>> "))
                if q == 1:
                    Three_D.Frustum.volume(r(), big_r(), h())

                elif q == 2:
                    Three_D.Frustum.csa(r(), big_r(), l())

                elif q == 3:
                    Three_D.Frustum.tsa(r(), big_r(), l())

                elif q == 4:
                    Three_D.Frustum.slant_height(r(), big_r(), h())

                else:
                    print("Something is wrong... Try Again!!!")
                    continue

            elif n == '8' or n == 'square' or n == 'Square':  # Square
                q = int(input("\nWhat do you want to find in Square?... \n1. Area\n2. Parameter\n>>> "))
                if q == 1:
                    Two_D.Square.area(a())

                elif q == 2:
                    Two_D.Square.parimeter(a())

                else:
                    print("Something is wrong... Try Again!!")
                    continue

            elif n == '9' or n == 'rectangle' or n == 'Rectangle':  # Rectangle
                q = int(input("\nWhat do you want to find in Rectange?... \n1. Area\n2. Parameter\n>>> "))
                if q == 1:
                    Two_D.Rectangle.area(l(), b())

                elif q == 2:
                    Two_D.Rectangle.parimeter(l(), b())

                else:
                    print("Something is wrong... Try Again!!")
                    continue

            elif n == '10' or n == 'circle' or n == 'Circle':  # Circle
                q = int(
                    input("\nWhat do you want to find in Circle?... \n1. Area\n2. Diameter\n3. Circumference\n>>> "))
                if q == 1:
                    Two_D.Circle.area(r())

                elif q == 2:
                    Two_D.Circle.diameter(r())

                elif q == 3:
                    Two_D.Circle.circumference(r())

                else:
                    print("Something is wrong... Try Again!!")
                    continue

            elif n == '11' or n == 'triangle' or n == 'Triangle':  # Triangle
                q = int(input("\nWhat do you want to find in Triangle?... \n1. Area\n2. Parameter\n>>> "))
                if q == 1:
                    Two_D.Triangle.area(b(), h())

                elif q == 2:
                    Two_D.Triangle.Parameter(l(), b(), h())

                else:
                    print("Something is wrong... Try Again!!")
                    continue

            else:
                print("Invalid!!... Try Again!!")
                continue

    except:
        print("Invalid!!!")
