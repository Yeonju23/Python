person, m = map(int, input().split())
people = list(map(int,input().split()))

party = person * m
for i in people:
    print(i - party,end=' ')

# 입력받은 참가자의 수 - person과 m을 곱한값(참가자의 수) 

