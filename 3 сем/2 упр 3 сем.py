# упражнение 2

def factor(n, a = []):
    for i in range(2,n):
        if n%i == 0:
            a.append(i)
            return factor(n//i,a)
    a.append(n)
    return a
print(factor(115))

def factor (n, i=2):
    while (i**2 <= n):
        if n%i:
            i += 1
        else:
            return [i] + factor(n//i, i)
    return [n]
print(factor(115))
