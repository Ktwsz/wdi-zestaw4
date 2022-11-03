def foo(t):
    m = [0 for i in range(len(t)*len(t))]
    ix = [0 for i in range(len(t))]

    ctr = 0
    while ctr < len(t)*len(t):
        mn, ix_mn = 2137, -1
        for i in range(n):
            if ix[i] < len(t) and t[i][ix[i]] < mn:
                mn = t[i][ix[i]]
                ix_mn = i

        m[ctr] = mn
        ix[ix_mn] += 1
        ctr += 1

    return m



n = int(input())

t = [[int(i) for i in input().split()] for j in range(n)]

print(foo(t))
