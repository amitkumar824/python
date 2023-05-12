line = "_"*75
while True:

    a11 = int(input())
    a12 = int(input())
    a13 = int(input())
    a21 = int(input())
    a22 = int(input())
    a23 = int(input())
    a31 = int(input())
    a32 = int(input())
    a33 = int(input())
    
    b11 = int(input())
    b12 = int(input())
    b13 = int(input())
    b21 = int(input())
    b22 = int(input())
    b23 = int(input())
    b31 = int(input())
    b32 = int(input())
    b33 = int(input())
    
    
    print(a11 * b11 + a12 * b21 + a13 * b31, (a11 * b12 + a12 * b22 + a13 * b32), (a11 * b13 + a12 * b23 + a13 * b33))
    print(a21 * b11 + a22 * b21 + a23 * b31, (a21 * b12 + a22 * b22 + a23 * b32), (a21 * b13 + a22 * b23 + a23 * b33))
    print(a31 * b11 + a32 * b21 + a33 * b31, (a31 * b12 + a32 * b22 + a33 * b32), (a31 * b13 + a32 * b23 + a33 * b33))
    print(line)