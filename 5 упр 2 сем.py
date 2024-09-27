# 5 упр
lst = list(map(int, input().split()))
new_lst = lst[1:] + lst[:1]
print (new_lst)