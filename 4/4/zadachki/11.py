n=int(input())
sum=0
sum2=0
for i in range(1,n+1):
   sum+=i
for i in range(1,n):
    i=int(input())
    sum2+=i
a=sum-sum2
print(a)