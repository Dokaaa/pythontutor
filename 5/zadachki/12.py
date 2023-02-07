s=str(input())
t=str('')
for i in range(len(s)):
    if i % 3 != 0:
        t+=s[i]
print(t)