n = int(input())
list = []
for i in range(n):
    s = input()
    if s == 1: continue
    elif s % s == 0: list.append(s)
    