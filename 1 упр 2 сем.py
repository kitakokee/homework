# 1 упр
a = list(map(int, input().split()))
n = a[0]
l = a[1:]
res = 0
for i in range(n+1):
    res ^= i
for i in l:
    res ^= i
print (res)
