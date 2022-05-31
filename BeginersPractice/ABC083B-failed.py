n, a, b = map(int, input().split())

Num_10000 = 0
Num_1000 = 0
Num_100 = 0
Num_10 = 0
Num_1 = 0

x = 0
lst = []
for s in list(str(n)):
    s = int(s)
    if s == 0:
        s = 9
    lst.append(s) 

if n == 10000:
    for h in range(2):
        Num_10000 = h
        for i in range(0,lst[1]+1):
            Num_1000 = i
            for j in range(0,lst[2]+1):
                Num_100 = j
                for k in range(0,lst[3]+1):
                    Num_10 =  k
                    for l in range(0,lst[4]+1):
                        Num_1 =  l
                        result = Num_10000 + Num_1000 + Num_100 + Num_10 + Num_1
                        if a <= result<= b:
                            if (10000 * Num_10000) + (1000 * Num_1000) + (100 * Num_100) + (10 * Num_10) + Num_1 <= n:
                                x = x + ((10000 * Num_10000) + (1000 * Num_1000) + (100 * Num_100) + (10 * Num_10) + Num_1)
elif 1000 < n < 10000:
    for i in range(0,lst[0]+1):
        Num_1000 = i
        for j in range(0,lst[1]+1):
            Num_100 = j
            for k in range(0,lst[2]+1):
                Num_10 =  k
                for l in range(0,lst[3]+1):
                    Num_1 =  l
                    result = Num_1000 + Num_100 + Num_10 + Num_1
                    if a <= result <= b:
                        if ((1000 * Num_1000) + (100 * Num_100) + (10 * Num_10) + Num_1 )<= n:
                            x = x + ((1000 * Num_1000) + (100 * Num_100) + (10 * Num_10) + Num_1)
elif n == 1000:
    for i in range(2):
        Num_1000 = i
        for j in range(0,lst[0]+1):
            Num_100 = j
            for k in range(0,lst[1]+1):
                Num_10 =  k
                for l in range(0,lst[2]+1):
                    Num_1 =  l
                    result = Num_1000 + Num_100 + Num_10 + Num_1
                    if a <= result<= b:
                        if (1000 * Num_1000) + (100 * Num_100) + (10 * Num_10) + Num_1 <= n:
                            x = x + ((1000 * Num_1000) + (100 * Num_100) +(10 * Num_10) + Num_1)
elif 100 < n < 1000:
    for j in range(0,lst[0]+1):
        Num_100 = j
        for k in range(0,lst[1]+1):
            Num_10 =  k
            for l in range(0,lst[2]+1):
                Num_1 =  l
                result = Num_100 + Num_10 + Num_1
                if a <= result<= b:
                    if (100 * Num_100) + (10 * Num_10) + Num_1 <= n:
                        x = x + ((100 * Num_100) +(10 * Num_10) + Num_1)
elif n == 100:
    for j in range(2):
        Num_100 = j
        for k in range(0,lst[1]+1):
            Num_10 =  k
            for l in range(0,lst[2]+1):
                Num_1 =  l
                result = Num_100 + Num_10 + Num_1
                if a <= result<= b:
                    if (100 * Num_100) + (10 * Num_10) + Num_1 <= n:
                        x = x + ((100 * Num_100) +(10 * Num_10) + Num_1)
elif 10 < n < 100:
    for k in range(0,lst[0]+1):
        Num_10 =  k
        for l in range(0,lst[1]+1):
            Num_1 =  l
            result = Num_10 + Num_1
            if a <= result<= b:
                if (10 * Num_10) + Num_1 <= n:
                    x = x + ((10 * Num_10) + Num_1)
elif n == 10:
    for k in range(2):
        Num_10 =  k
        for l in range(0,9):
                Num_1 =  l
                result = Num_10 + Num_1
                if a <= result<= b:
                    if (10 * Num_10) + Num_1 <= n:
                        x = x + ((10 * Num_10) + Num_1)
elif n < 10:
    for l in range(0,lst[0]):
                Num_1 =  l
                result =  Num_1
                if a <= result<= b:
                    if Num_1 <= n:
                        x = x + Num_1
                                                

print(x) 