def foo(n):
    t = [[0 for _ in range(n)] for _ in range(n)]

    l = 1
    for i in range(0, n):
        t[0][i] = l
        l += 1

    r = n-1
    i = 3
    v = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    x, y = 0, n-1
    while r > 0:
        for j in range(2):
            for k in range(r):
                x += v[i][0]
                y += v[i][1]
                t[x][y] = l
                l += 1
            i = (i-1)%4
        r -= 1


    return t



n = 2
t = foo(n)
for i in range(n):
    for j in range(n):
        print(t[i][j], end="")
        print(" ", end="")
    print("")
