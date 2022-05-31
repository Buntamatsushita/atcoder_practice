n = input()
S_n = str(n)
x = 0
for i in range(3):
    if S_n[i] == "1":
        x = x + 1
print(x)