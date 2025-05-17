#3. Восстановить строку по z-функции

alphabet = '$abcdefghijklmnopqrstuvwxyz'
def restore_string_from_z_function_with_alphabet(z_function, alphabet):

    n = len(z_function)
    s = [''] * n  
    pos = {char: i for i, char in enumerate(alphabet)}

    
    s[0] = alphabet[0] 
    used_chars = set([alphabet[0]])

    for i in range(1, n):
        if z_function[i] == 0:
            

            next_char = None
            for char in alphabet: 
                if char not in used_chars:
                    next_char = char
                    break

            if next_char is None: 
                next_char = alphabet[0] 

            s[i] = next_char
            used_chars.add(next_char)

        else:
            
            for j in range(z_function[i]):
                s[i + j] = s[j]


            if i + z_function[i] < n:
                if s[z_function[i]] == s[i + z_function[i]]:
                    return None

                next_char = None
                for char in alphabet:
                    if char != s[z_function[i]]:
                        next_char = char
                        break

                if next_char is None:  
                    return None
                if s[i + z_function[i]] == '': 
                    s[i + z_function[i]] = next_char
                    used_chars.add(next_char)


    return "".join(s)



zf = input("Z: ")

try:
    z = [int(x) for x in zf.split()]
except:
    print("Error")
    exit()

r = restore_string_from_z_function_with_alphabet(z, alphabet)
if r: print("S:", r)
else: print("No")
