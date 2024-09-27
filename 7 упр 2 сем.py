# 7

lst = list(map(int, input().split()))
max_numb = 0
res = 0
for i in lst:
    count = lst.count(i)
    if count > max_numb:
        max_numb = count
        res = i
print(res)