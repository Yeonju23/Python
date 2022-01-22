# 최대 공약수 구하기
def gcd(a,b):
    i = min(a,b) # 두 수 중에서 최솟값을 구하는 파이썬 함수

    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1

# gcd(a,b) = gcd(b, a%b)

def u_gcd(a,b):
    if b == 0:
        return a
    return u_gcd(a, a % b)