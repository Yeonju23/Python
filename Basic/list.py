# 자주 사용하는 리스트 기능
# len(a), pop(i), clear(), x in a
# append(x): 자료 x를 리스트 맨 뒤에 추가
# insert(i, x): 리스트의 i번 위치에 x를 추가

def find_max(a): #O(n)
    n = len(a)
    max = a[0]

    for i in range(0, n):
        if a[i] > max: # 최댓값을 찾기 위해서 비교를 n-1번 해야하기 때문
            max = a[i]
    return max

def find_max_index(a):
    n = len(a)
    max = 0

    for i in range(0,n):
        if a[i] > a[max]:
            max = i

    return max

def find_min(a):
    n = len(a)
    min = a[0]

    for i in range(0,n):
        if a[i]< min:
            min = a[i]
    return min

v = [17,28,34,6,432,5]
print(find_min(v))