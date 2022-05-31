c500 = int(input())
c100 = int(input())
c50 = int(input())
X = int(input())
x = X
N = 0
for i in range(c500 + 1):
    x1 = x - (500 * i)
    for j in range(c100 + 1):
        x2 = x1 - (100 * j)
        for k in range(c50 + 1):
            x3 = x2 - (50 * k)
            if x3 == 0:
                N = N + 1
print(N)