# 2 упр
input_data = input().split()
G = int(input_data[0]) 
s = input_data[1]       

length = len(s)
group_size = length // G

result = ""

for i in range(G):
    group = s[i * group_size:(i + 1) * group_size]
    result += group[::-1]

print(result)