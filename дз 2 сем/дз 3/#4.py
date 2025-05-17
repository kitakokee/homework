#4. Восстановить строку по префикс функции

def восстановить_строку(pi):

  n = len(pi)
  s = [''] * n  
  for i in range(n):

    if pi[i] > 0:
      if s[i] == '' and s[pi[i]-1] == '':
          continue 

      if s[i] == '':
        s[i] = s[pi[i]-1]
      elif s[pi[i]-1] == '':
        s[pi[i]-1] = s[i]
      elif s[i] != s[pi[i]-1]:
          return None 

    if s[i] == '':
      used_chars = set(s[:i])
      for char_code in range(ord('a'), ord('z') + 1): 
        char = chr(char_code)
        if char not in used_chars:
          s[i] = char
          break
      else:
        for char_code in range(ord('a'), ord('z') + 1): 
          char = chr(char_code)
          s[i] = char
          break
        else:
          return None 

  return "".join(s)


if __name__ == "__main__":
    try:

        pi = list(map(int, input_str.split()))

        # Восстановление строки
        s = восстановить_строку(pi)

        if s:
            print(s)
        else:
            print("невозможно восстановить строку для данной префикс-функции")
