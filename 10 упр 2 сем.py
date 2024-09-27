#10
s = input()

vowels = 'аоеёиуыэюяAOЕЁИУЫЭЮЯ'
result = ""

for i in range(len(s)):
    result += s[i]

    if s[i] in vowels:
        if i > 0 and s[i - 1] not in vowels:
            previous_vowel = s[i]
            result += 'с' + previous_vowel

print(result)