t = int(input())
li = []
for i in range(t):
    a, b = map(int,input().split())
    result = a+b
    li.append(result)

for i in range(t):
    print(li[i])
