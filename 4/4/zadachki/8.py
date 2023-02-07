n=int(input())
sum=1
total=0
for i in range (1,n+1):
    sum*=i
    total+=sum
print(total)