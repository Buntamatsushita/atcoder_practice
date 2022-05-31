n = int(input())
n_list = list(map(int, input().split()))
Even = n
N_times = 0
while Even == n:
    Even = 0
    for i in n_list:
        if (i % 2) == 0:
            Even = Even + 1
    if Even == n:
        for i in range(n-1):
            n_list[i] = n_list[i] / 2
        N_times = N_times + 1
    else:
        break
        
print(N_times)