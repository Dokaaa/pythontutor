prev = -1
curr = 0
max = 0
element = int(input())
while element != 0:
    if prev == element:
        curr += 1
    else:
        prev = element
        max = max(max, curr)
        curr = 1
    element = int(input())
max = max(max, curr)
print(max)

