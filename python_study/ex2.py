# 집합 자료형
s1 = set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)

l1 = list(s1)
print(l1)

l2 = tuple(s1)
print(l2)

#교집합, 합집합, 여집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
s1.intersection(s2)

print(s1 | s2)
s1.union(s2)

print(s1 - s2)