def PascalTriangle(n):
    trow = [1]
    y = [0]
    k = 2 * n - 2
    for x in range(n):
        for i in range(0, k):
            print
        print(trow)
        trow = [left + right for left, right in zip(trow + y, y + trow)]
    return n >= 1


PascalTriangle(5)
