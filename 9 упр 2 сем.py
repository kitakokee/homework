# 9
f= open ("input.txt", 'r')
lines = f.readlines()
a = list(map(str, lines[0].split()))
count = 0
for i in range(len(lines)):
    if '.' in lines[i] or '!' in lines[i] or '?' in lines[i]:
        count += 1
print(count)
f.close()