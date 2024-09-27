# 6 упр
lst = list(map(int, input().split()))
for i in lst:
    if lst.count(i) == 1:
       print(i)