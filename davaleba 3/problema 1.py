s = 'azcbobobegghakl'
test = s[0]
best = ""

for i in range(1, len(s)):

    if len(test) > len(best):
        best = test
    if s[i] >= s[i - 1]:
        test = test + s[i]
    else:
        test = s[i]

print(best)
