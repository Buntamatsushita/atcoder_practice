n, a, b = map(int, input().split())

answer = 0
def find(j):
    s = str(j)
    array = list(map(int, s))
    return sum(array)

for i in range(n + 1):
    x = find(i)
    if a <= x <= b:
        answer = answer + x
print(answer)        
        
