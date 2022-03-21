# a,b,c,d,e = map(int,input().split())

# v = ((a*a)+(b*b)+(c*c)+(d*d)+(e*e))%10

# print(v)

user_input = list(map(int, input().split()))
verify = 0

for i in user_input:
    verify += i * i

print(verify % 10)