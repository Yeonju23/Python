# 집합: 리스트와 같이 정보를 여러 개 넣어서 보관할 수 있는 파이썬의 기능
# 집합 하나에는 같은 자료가 중복되어 들어가지 않고, 자료의 순서도 의미가 없음
'''
s = set()

len(s), clear(), x in s
add(x): 집합에 자료 x를 추가
discard(x): 집합에 자료 x가 들어잇다면 삭제, 없으면 변화 없음
'''

# 동명이인 찾기 알고리즘
def find_same_name(a): # O(n^2)
     n = len(a)
     result = set()

     for i in range(0,n-1): # 리스트의 마지막 이름을 기준으로는 비교하지 않아도 됨. 자신의 뒤에는 비교할 이름이 없고, 앞과는 이미 비교가 끝났기 때문
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
     return result

def print_pairs(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i + 1, n):
            print(a[i],"-",a[j])

name = ['Tom', 'Sally', 'Jane']
print(print_pairs(name))