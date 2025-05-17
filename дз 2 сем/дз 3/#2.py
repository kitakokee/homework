#2. Посчитать количество вхождений строки и всех ее циклических сдвигов в текст

alphabet = '$abcdefghijklmnopqrstuvwxyz'
pos = {}
c = 0
for i in alphabet:
    pos[i] = c
    c += 1

def calc_position(count):
    for i in range(1,len(count)):
        count[i] += count[i-1]
    return count

def suff_array(s):
    s = s + '$'
    count = [0]*len(alphabet)
    for char in s:
        count[pos[char]] += 1
    count = calc_position(count)
    p = [0]*len(s)
    for i in range(len(s)-1,-1,-1):
        count[pos[s[i]]] -= 1
        p[count[pos[s[i]]]] = i
    c = [0]*len(s)
    cn = 0
    last_char = '$'
    for i in range(len(p)):
        if s[p[i]] != last_char:
            last_char = s[p[i]]
            cn += 1
        c[p[i]] = cn
    cur_len = 1
    while cur_len < len(s):
        sorted2 = [0]*len(s)
        for i in range(len(s)):
            sorted2[i] = (p[i] - cur_len + len(s))%len(s)
        count = [0]*len(s)
        for i in sorted2:
            count[c[i]] += 1
        count = calc_position(count)
        p_new = [0]*len(s)
        for i in range(len(sorted2)-1,-1,-1):
            count[c[sorted2[i]]] -= 1
            p_new[count[c[sorted2[i]]]] = sorted2[i]
        p = p_new
        new_c = [0]*len(s)
        cN = 0
        new_c[p[0]] = 0
        for i in range(1,len(p)):
            mid1 = (p[i] + cur_len)%len(s)
            mid2 = (p[i-1] + cur_len)%len(s)
            if c[p[i]] != c[p[i-1]] or c[mid1] != c[mid2]:
                cN += 1
            new_c[p[i]] = cN
        c = new_c
        cur_len *= 2
    return p

def count_cyclic_shifts_with_suffix_array(text, pattern):
    count = 0
    n = len(pattern)
    for i in range(n):
        shifted_pattern = pattern[i:] + pattern[:i]
        suffix_array_text = suff_array(text)
        left, right = 0, len(suffix_array_text) - 1
        first_occurrence = -1
        while left <= right:
            mid = (left + right) // 2
            suffix = text[suffix_array_text[mid]:]
            if suffix.startswith(shifted_pattern):
                first_occurrence = mid
                right = mid - 1
            elif suffix < shifted_pattern:
                left = mid + 1
            else:
                right = mid - 1
        if first_occurrence != -1:
            left, right = first_occurrence, len(suffix_array_text) - 1
            last_occurrence = first_occurrence
            while left <= right:
                mid = (left + right) // 2
                suffix = text[suffix_array_text[mid]:]
                if suffix.startswith(shifted_pattern):
                    last_occurrence = mid
                    left = mid + 1
                elif suffix < shifted_pattern:
                    left = mid + 1
                else:
                    right = mid - 1
            count += (last_occurrence - first_occurrence + 1)
    return count

text = input()
pattern = input()
result = count_cyclic_shifts_with_suffix_array(text, pattern)
