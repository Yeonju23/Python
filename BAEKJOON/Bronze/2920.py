li = list(map(int,input().split()))
a = []
for i in range(1,9):
    a.append(i)

b = a[::-1]

if a == li:
    print("ascending")
elif b == li: 
    print("descending")
else: print("mixed")