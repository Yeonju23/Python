import math as m

d, h, w = map(int, input().split())
q = m.sqrt(d**2/(h**2+w**2))
#q = d / ((h ** 2 + w ** 2) ** 0.5)
print(int(h * q), int(w * q))