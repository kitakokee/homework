# упр 3
s = input()

regular_palindrome = s == s[::-1]

mirror_dict = {
    'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', '1': '1', '8': '8',
    'E': '3', 'J': 'L', 'S': '2', 'Z': '5', '3': 'E', '2': 'S', '5': 'Z', 'L': 'J'}

mirror = True
for i in s:
    if i not in mirror_dict:
        mirror = False
        break

mirror_string = True
for i in range(len(s)):
    if s[i] != mirror_dict.get(s[i], None):
        mirror_string = False
        break

if not mirror and not regular_palindrome:
    result = f'"{s} is not a palindrome."'
elif regular_palindrome and not mirror:
    result = f'"{s} is a regular palindrome."'
elif mirror and not mirror_string:
    result = f'"{s} is a mirrored string."'
elif regular_palindrome and mirror and mirror_string:
    result = f'"{s} is a mirrored palindrome."'
else:
    result = f'"{s} is not a palindrome."'

print(result)