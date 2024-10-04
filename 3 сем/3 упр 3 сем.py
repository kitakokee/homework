# 3 упр
def evklid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = evklid(b, a % b)
        return d, y, x - y * (a // b)
    
print(evklid(4,6))