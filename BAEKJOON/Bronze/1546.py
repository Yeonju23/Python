n = int(input())
sub = list(map(int,input().split()))
max = max(sub)

for i in range(n):
    sub[i] = sub[i]/max*100
print(sum(sub)/n)

