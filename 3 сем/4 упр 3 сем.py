#упражднение 4 

#не через рекурсию
def triangle(size, symb):
    i = 1
    while (i < size/2):
        print(i*symb)
        i += 1
    if i == size/2:
        print(i*symb)
    while (i >= 1):
        print (i*symb)
        i -= 1
print(triangle(7,'*'))

#через рекурсию

def triangle(size ,symb , cur = 1):
    if size == 0:
        return
    print(min(cur,size)*symb)
    triangle(size-1, symb, cur + 1)

print(triangle(7, '*'))

