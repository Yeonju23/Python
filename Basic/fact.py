def fact(n):
    f = 1
    for i in range(1, n+1): #1부터 n까지
        f = f * i
    return f

#재귀 호출(recursion)
def hello():
    print("Hello")
    hello()

# n! = n x (n-1)!

def fact_2(n): #O(n)
    if n < 1 :
        return 1
    return n * fact_2(n-1)