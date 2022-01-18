def sum_n(n): # 덧셈 n번, O(n)
    s = 0
        
    for i in range(0,n+1):
        s = s + i
    return s 

def sum_m(m): #덧셈, 나눗셈, 곱셈 각 한번 (총 세 번), O(1)
    return m * (m+1) // 2 #입력 크기 m과 계산 시간이 더 늘어나지 않기 때문

# O(n): 필요한 계산 횟수가 입력 크기 n과 비례할 때
# O(1): 필요한 계산 횟수가 입력 크기 n과 무관할 때

# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램
def squared(n):
    s = 0

    for i in range(1, n+1):
        s = (i*i) + s
    return s

def squared_r(n):
    return (n*(n+1)*((2*n)+1))//6
