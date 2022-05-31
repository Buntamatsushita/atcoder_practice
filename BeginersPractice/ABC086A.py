n1, n2 = map(int, input().split())
r_n = n1 * n2

if (r_n % 2) != 0 :
    print("Odd")
else:
    print("Even")