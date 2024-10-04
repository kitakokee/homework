#упражнение 1 

#1 способ 
def fib(n):
    if n in [0, 1]:
        return n
    return (fib(n-1) + fib(n-2))

print (fib(9))

#2 cпособ
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = a+b, a
    return a
print(fib(9))

#3 cпособ

def fib(n, c = {0:0, 1:1}):
    if n in c:
        return c[n]
    c[n]= fib(n-1) + fib(n-2)
    return c[n]
print(fib(9))