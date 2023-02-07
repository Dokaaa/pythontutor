s = input()
a = s[:s.find('h') + 1] 
b = s[s.rfind('h'):]
c = s[s.find('h') + 1:s.rfind('h')]
s = a + c.replace('h', 'H') + b
print(s)