# a = int(input())
# b = int(input())


# #방법 1: 나머지 이용
# print(a * (b%10))
# print(a * ((b%100)//10))
# print(a * ((b%1000)//100))
# print(a*b)


#방법 2: range(시작,끝, 순서)이용해 역순으로 출력
a = int(input())
b = input()

for i in range(len(b),0,-1):
    print(a*int(b[i-1]))

print(a*int(b))