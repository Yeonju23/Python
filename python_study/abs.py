import math

def abs_sign(a):
    if a >= 0:
        return a
    else: return -a

# math.square()은 소수점이 붙은 값을 돌려줌
def abs_square(a):
    b = a*a
    return math.sqrt(b)

print(abs_sign(5))
print(abs_sign(-3))
print()
print(abs_square(5))
print(abs_square(5))